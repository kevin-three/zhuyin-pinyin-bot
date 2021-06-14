#!/usr/bin/env python

import os
import dotenv
import discord

from pyzh import convert

dotenv.load_dotenv()

client = discord.Client()

trigger = "↔️"

def get_trigger():
    return trigger

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == get_trigger():
        channel = client.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        await channel.send(convert(msg.content), reference=msg)

client.run(os.getenv("TOKEN"))

