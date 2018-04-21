# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

import sys
from hashlib import sha1

from django.db import models


class AccountBanHistory(models.Model):
    account = models.ForeignKey('Accounts', models.DO_NOTHING)
    reason = models.CharField(max_length=255)
    banned_at = models.BigIntegerField()
    expired_at = models.BigIntegerField()
    banned_by = models.ForeignKey('Players', models.DO_NOTHING, db_column='banned_by')

    class Meta:
        db_table = 'account_ban_history'


class AccountBans(models.Model):
    account = models.ForeignKey('Accounts', models.DO_NOTHING, primary_key=True)
    reason = models.CharField(max_length=255)
    banned_at = models.BigIntegerField()
    expires_at = models.BigIntegerField()
    banned_by = models.ForeignKey('Players', models.DO_NOTHING, db_column='banned_by')

    class Meta:
        db_table = 'account_bans'


class AccountViplist(models.Model):
    account = models.ForeignKey('Accounts', models.DO_NOTHING)
    player = models.ForeignKey('Players', models.DO_NOTHING)
    description = models.CharField(max_length=128)
    icon = models.PositiveIntegerField()
    notify = models.IntegerField()

    class Meta:
        db_table = 'account_viplist'
        unique_together = (('account', 'player'),)


class Accounts(models.Model):
    name = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=40)
    secret = models.CharField(max_length=16, blank=True, null=True)
    type = models.IntegerField()
    premdays = models.IntegerField()
    lastday = models.PositiveIntegerField()
    email = models.CharField(max_length=255)
    creation = models.IntegerField()

    def save(self, *args, **kwargs):
	    self.password = sha1(str(self.password).encode('utf8')).hexdigest()
	    print("SHA1 password : "+str(self.password), file=sys.stderr)
	    super(Accounts, self).save(*args, **kwargs)

    class Meta:
        db_table = 'accounts'


class GuildInvites(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    guild = models.ForeignKey('Guilds', models.DO_NOTHING)

    class Meta:
        db_table = 'guild_invites'
        unique_together = (('player', 'guild'),)


class GuildMembership(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    guild = models.ForeignKey('Guilds', models.DO_NOTHING)
    rank = models.ForeignKey('GuildRanks', models.DO_NOTHING)
    nick = models.CharField(max_length=15)

    class Meta:
        db_table = 'guild_membership'


class GuildRanks(models.Model):
    guild = models.ForeignKey('Guilds', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    level = models.IntegerField()

    class Meta:
        db_table = 'guild_ranks'


class GuildWars(models.Model):
    guild1 = models.IntegerField()
    guild2 = models.IntegerField()
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    status = models.IntegerField()
    started = models.BigIntegerField()
    ended = models.BigIntegerField()

    class Meta:
        db_table = 'guild_wars'


class Guilds(models.Model):
    name = models.CharField(unique=True, max_length=255)
    ownerid = models.ForeignKey('Players', models.DO_NOTHING, db_column='ownerid', unique=True)
    creationdata = models.IntegerField()
    motd = models.CharField(max_length=255)

    class Meta:
        db_table = 'guilds'


class GuildwarKills(models.Model):
    killer = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    killerguild = models.IntegerField()
    targetguild = models.IntegerField()
    warid = models.ForeignKey(GuildWars, models.DO_NOTHING, db_column='warid')
    time = models.BigIntegerField()

    class Meta:
        db_table = 'guildwar_kills'


class HouseLists(models.Model):
    house = models.ForeignKey('Houses', models.DO_NOTHING)
    listid = models.IntegerField()
    list = models.TextField()

    class Meta:
        db_table = 'house_lists'


class Houses(models.Model):
    owner = models.IntegerField()
    paid = models.PositiveIntegerField()
    warnings = models.IntegerField()
    name = models.CharField(max_length=255)
    rent = models.IntegerField()
    town_id = models.IntegerField()
    bid = models.IntegerField()
    bid_end = models.IntegerField()
    last_bid = models.IntegerField()
    highest_bidder = models.IntegerField()
    size = models.IntegerField()
    beds = models.IntegerField()

    class Meta:
        db_table = 'houses'


class IpBans(models.Model):
    ip = models.PositiveIntegerField(primary_key=True)
    reason = models.CharField(max_length=255)
    banned_at = models.BigIntegerField()
    expires_at = models.BigIntegerField()
    banned_by = models.ForeignKey('Players', models.DO_NOTHING, db_column='banned_by')

    class Meta:
        db_table = 'ip_bans'


class MarketHistory(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    sale = models.IntegerField()
    itemtype = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    expires_at = models.BigIntegerField()
    inserted = models.BigIntegerField()
    state = models.PositiveIntegerField()

    class Meta:
        db_table = 'market_history'


class MarketOffers(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    sale = models.IntegerField()
    itemtype = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    created = models.BigIntegerField()
    anonymous = models.IntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        db_table = 'market_offers'


class PlayerDeaths(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    time = models.BigIntegerField()
    level = models.IntegerField()
    killed_by = models.CharField(max_length=255)
    is_player = models.IntegerField()
    mostdamage_by = models.CharField(max_length=100)
    mostdamage_is_player = models.IntegerField()
    unjustified = models.IntegerField()
    mostdamage_unjustified = models.IntegerField()

    class Meta:
        db_table = 'player_deaths'


class PlayerDepotitems(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    sid = models.IntegerField()
    pid = models.IntegerField()
    itemtype = models.SmallIntegerField()
    count = models.SmallIntegerField()
    attributes = models.TextField()

    class Meta:
        db_table = 'player_depotitems'
        unique_together = (('player', 'sid'),)


class PlayerInboxitems(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    sid = models.IntegerField()
    pid = models.IntegerField()
    itemtype = models.SmallIntegerField()
    count = models.SmallIntegerField()
    attributes = models.TextField()

    class Meta:
        db_table = 'player_inboxitems'
        unique_together = (('player', 'sid'),)


class PlayerItems(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    pid = models.IntegerField()
    sid = models.IntegerField()
    itemtype = models.SmallIntegerField()
    count = models.SmallIntegerField()
    attributes = models.TextField()

    class Meta:
        db_table = 'player_items'


class PlayerNamelocks(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    reason = models.CharField(max_length=255)
    namelocked_at = models.BigIntegerField()
    namelocked_by = models.ForeignKey('Players', models.DO_NOTHING, related_name='namelocked_by')

    class Meta:
        db_table = 'player_namelocks'


class PlayerSpells(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'player_spells'


class PlayerStorage(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    key = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        db_table = 'player_storage'
        unique_together = (('player', 'key'),)


class Players(models.Model):
    name = models.CharField(unique=True, max_length=255)
    group_id = models.IntegerField()
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    level = models.IntegerField()
    vocation = models.IntegerField()
    health = models.IntegerField()
    healthmax = models.IntegerField()
    experience = models.BigIntegerField()
    lookbody = models.IntegerField()
    lookfeet = models.IntegerField()
    lookhead = models.IntegerField()
    looklegs = models.IntegerField()
    looktype = models.IntegerField()
    lookaddons = models.IntegerField()
    maglevel = models.IntegerField()
    mana = models.IntegerField()
    manamax = models.IntegerField()
    manaspent = models.PositiveIntegerField()
    soul = models.PositiveIntegerField()
    town_id = models.IntegerField()
    posx = models.IntegerField()
    posy = models.IntegerField()
    posz = models.IntegerField()
    conditions = models.TextField()
    cap = models.IntegerField()
    sex = models.IntegerField()
    lastlogin = models.BigIntegerField()
    lastip = models.PositiveIntegerField()
    saveOT = models.IntegerField(db_column='save')
    skull = models.IntegerField()
    skulltime = models.IntegerField()
    lastlogout = models.BigIntegerField()
    blessings = models.IntegerField()
    onlinetime = models.IntegerField()
    deletion = models.BigIntegerField()
    balance = models.BigIntegerField()
    offlinetraining_time = models.PositiveSmallIntegerField()
    offlinetraining_skill = models.IntegerField()
    stamina = models.PositiveSmallIntegerField()
    skill_fist = models.PositiveIntegerField()
    skill_fist_tries = models.BigIntegerField()
    skill_club = models.PositiveIntegerField()
    skill_club_tries = models.BigIntegerField()
    skill_sword = models.PositiveIntegerField()
    skill_sword_tries = models.BigIntegerField()
    skill_axe = models.PositiveIntegerField()
    skill_axe_tries = models.BigIntegerField()
    skill_dist = models.PositiveIntegerField()
    skill_dist_tries = models.BigIntegerField()
    skill_shielding = models.PositiveIntegerField()
    skill_shielding_tries = models.BigIntegerField()
    skill_fishing = models.PositiveIntegerField()
    skill_fishing_tries = models.BigIntegerField()

    class Meta:
        db_table = 'players'


class PlayersOnline(models.Model):
    player_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'players_online'


class ServerConfig(models.Model):
    config = models.CharField(primary_key=True, max_length=50)
    value = models.CharField(max_length=256)

    class Meta:
        db_table = 'server_config'


class TileStore(models.Model):
    house = models.ForeignKey(Houses, models.DO_NOTHING)
    data = models.TextField()

    class Meta:
        db_table = 'tile_store'
