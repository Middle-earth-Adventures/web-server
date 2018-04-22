import json
import sys
import time
from hashlib import sha1

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Accounts, Players


# RENDERS ############################
def index(request):

    if request.method != "GET":
        print("not a GET request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    try:
        user = authenticate(request, username=request.session["username"], password=request.session["password"])
        if user is not None:
            login(request, user)
            return account(request)
    except Exception:
        pass

    return render(request, "index.html")


def account(request):

    if request.method != "GET":
        print("not a GET request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    try:
        user = authenticate(request, username=request.session["username"], password=request.session["password"])
        if user is None:
            return HttpResponse(status=403)
    except Exception:
        login(request, user)
        pass

    return render(request, "account.html")


# POST PROCESSORS ####################
def createAccount(request):

    if request.method != "POST":
        print("not a POST request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    accountData = json.loads(request.body.decode('utf8'))
    print("Account data\n\tEmail: "+accountData["email"]+"\n\tUser: " +
          accountData["user"]+"\n\tPassword: "+accountData["password"], file=sys.stderr)

    newAccount = Accounts(
        name=accountData["user"],
        password=accountData["password"],
        secret="",
        type=0,
        premdays=0,
        email=accountData["email"],
        lastday=0,
        creation=time.time()
    )
    newAccount.save()

    return HttpResponse(status=200)


def signin(request):

    if request.method != "POST":
        print("not a POST request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    # Authenticate OT data
    accountData = json.loads(request.body.decode('utf8'))
    print("Account data\n\tUser: "+accountData["user"]+"\n\tPassword: "+accountData["password"] +
          "\n\tencrypted Password: "+sha1(str(accountData["password"]).encode("utf8")).hexdigest(), file=sys.stderr)

    account = Accounts.objects.get(name__exact=accountData["user"], password__exact=sha1(
        str(accountData["password"]).encode("utf8")).hexdigest())  # DoesNotExistException

    # Create Django User, login an set session variables
    user = authenticate(request, username=account.name, password=account.password)
    if user is None:
        user = User.objects.create_user(account.name, account.email, account.password)

    login(request, user)

    request.session["username"] = account.name
    request.session["password"] = account.password
    return HttpResponse("/account", content_type="text/plain")


def signout(request):

    if request.method != "GET":
        print("not a GET request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    # Verify Session + Django User login and logout
    if "username" not in request.session or "username" not in request.session:
        # It can't just logout by username nor password, or can It?
        return render(request, "index.html")

    user = authenticate(request, username=request.session["username"], password=request.session["password"])
    if user is None:
        return render(request, "index.html")

    logout(request)
    return HttpResponse("/", content_type="text/plain")


def createPlayer(request):

    if request.method != "POST":
        print("not a POST request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    # Authorize Django User before considering player's creation

    user = authenticate(request, username=request.session["username"], password=request.session["password"])
    if user is None:
        print("not authorized to crete player: " + request.body, file=sys.stderr)
        return HttpResponse(status=403)

    playerData = json.loads(request.body.decode('utf8'))
    print("Player received data\n\tUser: "+request.session["username"] +
          "\n\tPlayer's name: "+playerData["name"], file=sys.stderr)

    # Verify if player already exists

    if len(Players.objects.filter(name__exact=playerData["name"])) != 0:
        return HttpResponse("1", content_type="text/plain", status=409)

    account = Accounts.objects.filter(name__exact=request.session["username"])
    if len(account) != 1:
        return HttpResponse("2", content_type="text/plain", status=409)

    newPlayer = Players(
        name=str(playerData["name"]),
        group_id=0,
        account=account[0],
        level=1,
        vocation=0,
        health=120,
        healthmax=120,
        experience=0,
        lookbody=0,
        lookfeet=0,
        lookhead=0,
        looklegs=0,
        looktype=0,
        lookaddons=0,
        maglevel=0,
        mana=20,
        manamax=20,
        manaspent=0,
        soul=100,
        town_id=0,
        posx=0,
        posy=0,
        posz=0,
        conditions="",
        cap=250,
        sex=0,
        lastlogin=0,
        lastip=0,
        saveOT=0,
        skull=0,
        skulltime=0,
        lastlogout=0,
        blessings=0,
        onlinetime=0,
        deletion=0,
        balance=0,
        offlinetraining_time=0,
        offlinetraining_skill=0,
        stamina=100,
        skill_fist=10,
        skill_fist_tries=0,
        skill_club=10,
        skill_club_tries=0,
        skill_sword=10,
        skill_sword_tries=0,
        skill_axe=10,
        skill_axe_tries=0,
        skill_dist=10,
        skill_dist_tries=0,
        skill_shielding=10,
        skill_shielding_tries=0,
        skill_fishing=0,
        skill_fishing_tries=0)
    newPlayer.save()

    return HttpResponse(status=200)


def getAccountsPlayers(request):

    if request.method != "GET":
        print("not a GET request: " + request.method, file=sys.stderr)
        return HttpResponse(status=400)

    # Authorize Django User before considering player's creation
    user = authenticate(request, username=request.session["username"], password=request.session["password"])
    if user is None:
        print("not authorized to list platers: " + request.body, file=sys.stderr)
        return HttpResponse(status=403)

    account = Accounts.objects.get(
        name__exact=request.session["username"], password__exact=request.session["password"])  # DoesNotExistException
    players = Players.objects.filter(account__exact=account)

    jsonPlayersData = serializers.serialize("json", players, fields=('name', 'level', 'stamina'))
    return JsonResponse(jsonPlayersData, safe=False)
