import discord
from discord.ext import tasks
from WebsiteUpdate import Website_Check

# replace with the token for your bot
token = "#"

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    send_message.start()

# replace with the time you would like to wait before each update is sent


@tasks.loop(seconds = x)
async def send_message():
    await client.wait_until_ready()
    channel = client.get_channel(DiscordChannelID)  # replace with channel_id
    check = Website_Check()
    check.checkWebsite()
    if check.changed == True:
        message = "Message to send in Discord Channel"
        await channel.send(message)

client.run(token)
