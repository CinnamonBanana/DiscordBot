import discord
import os
import secret
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&', intents=intents)


@bot.event
async def on_ready():
    print('------')
    print('Loading cogs:')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
            except discord.ClientException as e:
                print(f'!!!{filename} loading error! {e}')
                continue
    print('------')
    print(f'Connected as {bot.user.name}')
    print('id: {}'.format(bot.user.id))
    print('------')


bot.run(secret.TOKEN)
