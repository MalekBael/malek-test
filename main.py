import discord
import asyncio
import datetime

client = discord.Client()

distoken = ODY1MjczMzA3OTg0Mjk4MDE0.YPBmkA.oUYF0-hh9VxhGbDWuqAgvSLKOTc

# These must all be Voice Channels
timechannel = 865229417877340161 # The ID of the Channel that gets renamed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        now = datetime.datetime.now()
        await client.get_channel(timechannel).edit(name=f"{now.hour}:{now.minute} (<GB>)") # The channel gets changed here
        await asyncio.sleep(60)
client.run(distoken)