import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Huy B oc cho')

client.run('MTAxNDA2OTg0NzI3MDg4NzQyNA.GWf_AO.Er9k_jBEXXp8Tbux5D0UQ77BBArbW_fY3PVcXA')