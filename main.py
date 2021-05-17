import discord, time, datetime, os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

start_time = time.time()

client = commands.Bot(command_prefix="!!")
TOKEN = 'TOKEN_HERE'

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
  print(f"Bot started as {client.user.name}")

@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(color=discord.Color.green(), description=text)
    await ctx.send(embed=embed)

client.run(TOKEN, bot=True, reconnect=True)
