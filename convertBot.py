import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "")
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author.id != "435229925503533057":
        if message.content.lower().startswith("conv"):
            if message.content.lower().endswith("cm"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newF = old / 2.54
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "cm is " + toReturn + "in")
            if message.content.lower().endswith("in"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newF = old * 2.54
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "in is " + toReturn + "cm")
            if message.content.lower().endswith("c"):
                end = len(message.content) - 1
                old = float(message.content[4:end])
                newF = (old * 1.8) + 32
                toReturn = str(newF)
                await client.send_message(message.channel, message.content[4:end]+ "C is " + toReturn + "F")
            if message.content.lower().endswith("f"):
                end = len(message.content) - 1
                old = float(message.content[4:end])
                newC = (old - 32) / 1.8
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "F is " + toReturn + "C")    
            if message.content.lower().endswith("mi"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newC = old * 1.6
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "mi is " + toReturn + "km")
            if message.content.lower().endswith("miles"):
                end = len(message.content) - 5
                old = float(message.content[4:end])
                newC = old * 1.6
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "mi is " + toReturn + "km")
            if message.content.lower().endswith("km"):
                end = len(message.content) - 2
                old = float(message.content[4:end])
                newC = old * 0.62
                toReturn = str(newC)
                await client.send_message(message.channel, message.content[4:end]+ "km is " + toReturn + "mi")        


client.run("YOUR_TOKEN_HERE")
