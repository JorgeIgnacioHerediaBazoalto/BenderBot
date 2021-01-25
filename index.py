#!/usr/bin/env python
#_*_ coding: utf8 _*_

import discord
from discord.ext import commands
import random
import datetime
from youtube_search import YoutubeSearch
from playsound import playsound

TOKEN = 'NzY0MTI5NTQ0MzMyMzc4MTEy.X4BxGA.1iLEqI4OvmdP8dQe-TXJF_9U_Ew'
prefijo = '$'
bot = commands.Bot(command_prefix='$', description="Este es el bot Bender te ayudara en lo que necesites")
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name = 'Ayudar'))
    print("Bot Bender is ready")
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name}", description = "Estas en un servidor de Discord que decidio comprarme como su asistente, estare aqui para proporcionarte toda la informacion necesaria, y ayudarte en diversas acciones", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name = "Este server tiene el siguiente ID: ", value = f"{ctx.guild.id}")
    embed.add_field(name = "Este server pertenece a la region: ", value = f"{ctx.guild.region}")
    embed.add_field(name = "Este server pertenece al lider con ID: ", value = f"{ctx.guild.owner_id}")
    embed.add_field(name = "Este server fue creado el: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name = "Banner: ", value = f"{ctx.guild.banner}")
    embed.set_thumbnail(url = f"{ctx.guild.icon}")

    await ctx.send(embed=embed)

@bot.command()
async def srcY(ctx, *, search):
    resultados = []
    resul1 = YoutubeSearch(search, max_results=3).to_dict()
    for i in resul1:
        resultados.append(i['id'])

    for a in resultados:
        channel = ctx.channel
        await channel.send('https://www.youtube.com/watch?v=' + a)

@bot.command()
async def play(ctx, *, url):
    playsound(url)

@bot.listen()
async def on_message(ctx):
    saludo = ["Hola, ¿Que tal?","Hola, Bienvenido","Bola","Chibola"]
    despedida = ["Adios, cuidate", "Bye, que te vaya bien", "ByeBye"]
    jugar = ["Go @everyone", "Vamos, Vamos a JUGAR @everyone!!!", "Hey @everyone, {} nos llama".format(ctx.author)]
    num = random.randint(0,3)
    num2 = random.randint(0,2)

    if "hola" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(saludo[num])

    elif "hi" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(saludo[num])

    elif "hello" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(saludo[num])

    elif "adios" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(despedida[num2])

    elif "bye" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(despedida[num2])

    elif "juguemos" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(jugar[num2])

    elif "jugamos" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(jugar[num2])

    elif "go" in ctx.content.lower():
        if ctx.author==bot.user:
            return
        channel = ctx.channel
        await channel.send(jugar[num2]) 

bot.run(TOKEN)