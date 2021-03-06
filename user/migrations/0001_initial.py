# Generated by Django 2.0.1 on 2018-01-28 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBanHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('banned_at', models.BigIntegerField()),
                ('expired_at', models.BigIntegerField()),
            ],
            options={
                'db_table': 'account_ban_history',
            },
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('secret', models.CharField(blank=True, max_length=16, null=True)),
                ('type', models.IntegerField()),
                ('premdays', models.IntegerField()),
                ('lastday', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=255)),
                ('creation', models.IntegerField()),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='AccountViplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('icon', models.PositiveIntegerField()),
                ('notify', models.IntegerField()),
            ],
            options={
                'db_table': 'account_viplist',
            },
        ),
        migrations.CreateModel(
            name='GuildRanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
            options={
                'db_table': 'guild_ranks',
            },
        ),
        migrations.CreateModel(
            name='Guilds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('creationdata', models.IntegerField()),
                ('motd', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'guilds',
            },
        ),
        migrations.CreateModel(
            name='GuildwarKills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('killer', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=50)),
                ('killerguild', models.IntegerField()),
                ('targetguild', models.IntegerField()),
                ('time', models.BigIntegerField()),
            ],
            options={
                'db_table': 'guildwar_kills',
            },
        ),
        migrations.CreateModel(
            name='GuildWars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild1', models.IntegerField()),
                ('guild2', models.IntegerField()),
                ('name1', models.CharField(max_length=255)),
                ('name2', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('started', models.BigIntegerField()),
                ('ended', models.BigIntegerField()),
            ],
            options={
                'db_table': 'guild_wars',
            },
        ),
        migrations.CreateModel(
            name='HouseLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listid', models.IntegerField()),
                ('list', models.TextField()),
            ],
            options={
                'db_table': 'house_lists',
            },
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('paid', models.PositiveIntegerField()),
                ('warnings', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('rent', models.IntegerField()),
                ('town_id', models.IntegerField()),
                ('bid', models.IntegerField()),
                ('bid_end', models.IntegerField()),
                ('last_bid', models.IntegerField()),
                ('highest_bidder', models.IntegerField()),
                ('size', models.IntegerField()),
                ('beds', models.IntegerField()),
            ],
            options={
                'db_table': 'houses',
            },
        ),
        migrations.CreateModel(
            name='IpBans',
            fields=[
                ('ip', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('reason', models.CharField(max_length=255)),
                ('banned_at', models.BigIntegerField()),
                ('expires_at', models.BigIntegerField()),
            ],
            options={
                'db_table': 'ip_bans',
            },
        ),
        migrations.CreateModel(
            name='MarketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.IntegerField()),
                ('itemtype', models.PositiveIntegerField()),
                ('amount', models.PositiveSmallIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('expires_at', models.BigIntegerField()),
                ('inserted', models.BigIntegerField()),
                ('state', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'market_history',
            },
        ),
        migrations.CreateModel(
            name='MarketOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.IntegerField()),
                ('itemtype', models.PositiveIntegerField()),
                ('amount', models.PositiveSmallIntegerField()),
                ('created', models.BigIntegerField()),
                ('anonymous', models.IntegerField()),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'market_offers',
            },
        ),
        migrations.CreateModel(
            name='PlayerDeaths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.BigIntegerField()),
                ('level', models.IntegerField()),
                ('killed_by', models.CharField(max_length=255)),
                ('is_player', models.IntegerField()),
                ('mostdamage_by', models.CharField(max_length=100)),
                ('mostdamage_is_player', models.IntegerField()),
                ('unjustified', models.IntegerField()),
                ('mostdamage_unjustified', models.IntegerField()),
            ],
            options={
                'db_table': 'player_deaths',
            },
        ),
        migrations.CreateModel(
            name='PlayerDepotitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('itemtype', models.SmallIntegerField()),
                ('count', models.SmallIntegerField()),
                ('attributes', models.TextField()),
            ],
            options={
                'db_table': 'player_depotitems',
            },
        ),
        migrations.CreateModel(
            name='PlayerInboxitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('itemtype', models.SmallIntegerField()),
                ('count', models.SmallIntegerField()),
                ('attributes', models.TextField()),
            ],
            options={
                'db_table': 'player_inboxitems',
            },
        ),
        migrations.CreateModel(
            name='PlayerItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('itemtype', models.SmallIntegerField()),
                ('count', models.SmallIntegerField()),
                ('attributes', models.TextField()),
            ],
            options={
                'db_table': 'player_items',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('group_id', models.IntegerField()),
                ('level', models.IntegerField()),
                ('vocation', models.IntegerField()),
                ('health', models.IntegerField()),
                ('healthmax', models.IntegerField()),
                ('experience', models.BigIntegerField()),
                ('lookbody', models.IntegerField()),
                ('lookfeet', models.IntegerField()),
                ('lookhead', models.IntegerField()),
                ('looklegs', models.IntegerField()),
                ('looktype', models.IntegerField()),
                ('lookaddons', models.IntegerField()),
                ('maglevel', models.IntegerField()),
                ('mana', models.IntegerField()),
                ('manamax', models.IntegerField()),
                ('manaspent', models.PositiveIntegerField()),
                ('soul', models.PositiveIntegerField()),
                ('town_id', models.IntegerField()),
                ('posx', models.IntegerField()),
                ('posy', models.IntegerField()),
                ('posz', models.IntegerField()),
                ('conditions', models.TextField()),
                ('cap', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('lastlogin', models.BigIntegerField()),
                ('lastip', models.PositiveIntegerField()),
                ('save', models.IntegerField()),
                ('skull', models.IntegerField()),
                ('skulltime', models.IntegerField()),
                ('lastlogout', models.BigIntegerField()),
                ('blessings', models.IntegerField()),
                ('onlinetime', models.IntegerField()),
                ('deletion', models.BigIntegerField()),
                ('balance', models.BigIntegerField()),
                ('offlinetraining_time', models.PositiveSmallIntegerField()),
                ('offlinetraining_skill', models.IntegerField()),
                ('stamina', models.PositiveSmallIntegerField()),
                ('skill_fist', models.PositiveIntegerField()),
                ('skill_fist_tries', models.BigIntegerField()),
                ('skill_club', models.PositiveIntegerField()),
                ('skill_club_tries', models.BigIntegerField()),
                ('skill_sword', models.PositiveIntegerField()),
                ('skill_sword_tries', models.BigIntegerField()),
                ('skill_axe', models.PositiveIntegerField()),
                ('skill_axe_tries', models.BigIntegerField()),
                ('skill_dist', models.PositiveIntegerField()),
                ('skill_dist_tries', models.BigIntegerField()),
                ('skill_shielding', models.PositiveIntegerField()),
                ('skill_shielding_tries', models.BigIntegerField()),
                ('skill_fishing', models.PositiveIntegerField()),
                ('skill_fishing_tries', models.BigIntegerField()),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='PlayersOnline',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'players_online',
            },
        ),
        migrations.CreateModel(
            name='PlayerSpells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'player_spells',
            },
        ),
        migrations.CreateModel(
            name='ServerConfig',
            fields=[
                ('config', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'server_config',
            },
        ),
        migrations.CreateModel(
            name='TileStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Houses')),
            ],
            options={
                'db_table': 'tile_store',
            },
        ),
        migrations.CreateModel(
            name='AccountBans',
            fields=[
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Accounts')),
                ('reason', models.CharField(max_length=255)),
                ('banned_at', models.BigIntegerField()),
                ('expires_at', models.BigIntegerField()),
            ],
            options={
                'db_table': 'account_bans',
            },
        ),
        migrations.CreateModel(
            name='GuildInvites',
            fields=[
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Players')),
            ],
            options={
                'db_table': 'guild_invites',
            },
        ),
        migrations.CreateModel(
            name='GuildMembership',
            fields=[
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Players')),
                ('nick', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'guild_membership',
            },
        ),
        migrations.CreateModel(
            name='PlayerNamelocks',
            fields=[
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Players')),
                ('reason', models.CharField(max_length=255)),
                ('namelocked_at', models.BigIntegerField()),
            ],
            options={
                'db_table': 'player_namelocks',
            },
        ),
        migrations.CreateModel(
            name='PlayerStorage',
            fields=[
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Players')),
                ('key', models.PositiveIntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'db_table': 'player_storage',
            },
        ),
        migrations.AddField(
            model_name='playerspells',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='players',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Accounts'),
        ),
        migrations.AddField(
            model_name='playeritems',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='playerinboxitems',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='playerdepotitems',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='playerdeaths',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='marketoffers',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='markethistory',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='ipbans',
            name='banned_by',
            field=models.ForeignKey(db_column='banned_by', on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='houselists',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Houses'),
        ),
        migrations.AddField(
            model_name='guildwarkills',
            name='warid',
            field=models.ForeignKey(db_column='warid', on_delete=django.db.models.deletion.DO_NOTHING, to='user.GuildWars'),
        ),
        migrations.AddField(
            model_name='guilds',
            name='ownerid',
            field=models.ForeignKey(db_column='ownerid', on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players', unique=True),
        ),
        migrations.AddField(
            model_name='guildranks',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Guilds'),
        ),
        migrations.AddField(
            model_name='accountviplist',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Accounts'),
        ),
        migrations.AddField(
            model_name='accountviplist',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AddField(
            model_name='accountbanhistory',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Accounts'),
        ),
        migrations.AddField(
            model_name='accountbanhistory',
            name='banned_by',
            field=models.ForeignKey(db_column='banned_by', on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AlterUniqueTogether(
            name='playerstorage',
            unique_together={('player', 'key')},
        ),
        migrations.AddField(
            model_name='playernamelocks',
            name='namelocked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='namelocked_by', to='user.Players'),
        ),
        migrations.AlterUniqueTogether(
            name='playerinboxitems',
            unique_together={('player', 'sid')},
        ),
        migrations.AlterUniqueTogether(
            name='playerdepotitems',
            unique_together={('player', 'sid')},
        ),
        migrations.AddField(
            model_name='guildmembership',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Guilds'),
        ),
        migrations.AddField(
            model_name='guildmembership',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.GuildRanks'),
        ),
        migrations.AddField(
            model_name='guildinvites',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Guilds'),
        ),
        migrations.AlterUniqueTogether(
            name='accountviplist',
            unique_together={('account', 'player')},
        ),
        migrations.AddField(
            model_name='accountbans',
            name='banned_by',
            field=models.ForeignKey(db_column='banned_by', on_delete=django.db.models.deletion.DO_NOTHING, to='user.Players'),
        ),
        migrations.AlterUniqueTogether(
            name='guildinvites',
            unique_together={('player', 'guild')},
        ),
    ]
