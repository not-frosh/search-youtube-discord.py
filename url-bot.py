import discord
import asyncio
import re
import urllib
from urllib.parse import urlparse
from discord.ext import commands

bot = commands.Bot(command_prefix=>)

@bot.command(pass_context= True)
async def ping(ctx):
 await ctx.send('pong')

@bot.command(pass_context= True)
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

bot.run("TOKEN")
