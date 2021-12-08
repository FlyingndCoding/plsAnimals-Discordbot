import discord
from discord.ext import commands
import aiohttp
import os
from keep_alive import keep_alive
client = commands.Bot(command_prefix=["pls ","pls"])
TOKEN = os.environ["TOKEN"]

@client.event
async def on_command_error(ctx, error):
  await ctx.send(error)

@client.event
async def on_ready():
    print("Ready")


@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/cat')
        catjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/cat')
        factjson = await request2.json()

    embed = discord.Embed(title="Cat!", color=discord.Color.purple())
    embed.set_image(url=catjson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

    embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
    embed.set_image(url=dogjson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round(client.latency * 1000)}ms.')

@client.command()
async def bird(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/bird')
        birdjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/bird')
        factjson = await request2.json()

    embed = discord.Embed(title="Birb!", color=discord.Color.purple())
    embed.set_image(url=birdjson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)


@client.command()
async def panda(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/panda')
        pandajson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/panda')
        factjson = await request2.json()

    embed = discord.Embed(title="Panda!!", color=discord.Color.purple())
    embed.set_image(url=pandajson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)


@client.command()
async def koala(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/koala')
        koalajson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/koala')
        factjson = await request2.json()

    embed = discord.Embed(title="koala!!", color=discord.Color.purple())
    embed.set_image(url=koalajson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)


@client.command()
async def fox(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/fox')
        foxjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/fox')
        factjson = await request2.json()

    embed = discord.Embed(title="Fox!", color=discord.Color.purple())
    embed.set_image(url=foxjson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)




keep_alive()
client.run(TOKEN)