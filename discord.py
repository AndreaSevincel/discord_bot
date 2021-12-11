import discord
import os
import requests

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith("info_pls"):
        await message.channel.send("I Am A Bot Programmed by my Master Andrea Sevincel!")

    elif message.content.startswith("!github"):
        await message.channel.send("The Github is https://github.com/AndreaSevincel! Follow it or i will follow you.")

    elif message.content.startswith("!gungengangeungenaguena"):
        await message.channel.send("gungengangeungenaguena!")

    elif message.content.startswith("hi"):
        await message.channel.send("Hello")

    elif message.content.startswith("!Andrea"):
        await message.channel.send("j")





# copy your token from the developer portal
client.run('paste_the_token_here')
