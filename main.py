import discord
from discord.ext import (
        commands,
    )

token = input("token : ")
prefix = "-"

FekBot = discord.Client()   
FekBot = commands.Bot(
    description='FekBot autoleaver',
    command_prefix=prefix,
    self_bot=True
) 


@FekBot.event
async def on_connect():
    n = 0
    for channel in FekBot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            print(f"Left {channel.id} {n}")
            n = n + 1

FekBot.run(token, bot=False)
