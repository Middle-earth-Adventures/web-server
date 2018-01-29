import json
import time
import sys
from hashlib import sha1

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from .models import Accounts


def index(request):

	if (request.method != "GET"):
		print("not a GET request: " + request.method, file=sys.stderr)
		return render(request, "index.htm")	# maybe something smaller ?

	try:
		user = authenticate(request, username=request.session["username"], password=request.session["password"])
		if user is not None:
			return render(request, "account.htm")
	except:
		pass

	return render(request, "index.htm")

def createAccount(request):

	if (request.method != "POST"):
		print("not a POST request: " + request.method, file=sys.stderr)
		return HttpResponse("BAD REQUEST")

	accountData = json.loads(request.body.decode('utf8'))
	print("Account data\n\tEmail: "+accountData["email"]+"\n\tUser: "+accountData["user"]+"\n\tPassword: "+str(accountData["password"]).encode("utf8"), file=sys.stderr)
	
	newAccount = Accounts(
		name = accountData["user"],
		password = accountData["password"],
		secret = "",
		type = 0,
		premdays = 0,
		email = accountData["email"],
		lastday = 0,
		creation = time.time()
	)
	newAccount.save()

	return HttpResponse("ok")

def signin(request):

	if (request.method != "POST"):
		print("not a POST request: " + request.method, file=sys.stderr)
		return HttpResponse("BAD REQUEST")

	accountData = json.loads(request.body.decode('utf8'))
	print("Account data\n\tUser: "+accountData["user"]+"\n\tPassword: "+accountData["password"]+"\n\tencrypted Password: "+sha1(str(accountData["password"]).encode("utf8")).hexdigest(), file=sys.stderr)

	account = Accounts.objects.get(name__exact=accountData["user"], password__exact=sha1(str(accountData["password"]).encode("utf8")).hexdigest()) # DoesNotExistException

	user = authenticate(request, username=account.name, password=account.password)
	if user is None:
		user = User.objects.create_user(account.name, account.email, account.password)

	login(request, user)
		
	request.session["username"] = account.name
	request.session["password"] = account.password
	return render(request, "account.htm")
