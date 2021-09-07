import discord
import random
import json
import requests
import re
import asyncio
import secret
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&', intents=intents)
voice_client = None


async def play_sound(ctx, sound: str):
    global voice_client
    if voice_client:
        await voice_client.disconnect()
    try:
        channel = ctx.author.voice.channel
    except AttributeError:
        await ctx.channel.send('Ля, брателло, а ты где?!')
    voice_client = await channel.connect(reconnect=False)
    audio_source = await discord.FFmpegOpusAudio.from_probe(sound)
    voice_client.play(audio_source)
    while voice_client.is_playing():
        continue
    await asyncio.sleep(1)
    await voice_client.disconnect()


async def filter(ctx, embedColor, memavatar, url):
    embed = discord.Embed(color=embedColor)
    parts = str(memavatar).rsplit('?', 2)
    embed.set_image(url=f'{url}?avatar={parts[0]}')
    await ctx.send(embed=embed)


async def action(ctx, embedColor, target, text, url):
    author = ctx.message.author
    response = requests.get(url)
    await ctx.send(f'{author} {text} {target}')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=embedColor)
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print('------')
    print(f'Connected as {bot.user.name}')
    print('id: {}'.format(bot.user.id))
    print('------')


@bot.event
async def on_message(message):
    #print(f"Message: {message.content}")
    if message.author.id == bot.user.id:
        return
    reg_search = re.search(r'(i\'m|im|i am|я) (.{1,})$', message.content, re.IGNORECASE)
    if reg_search:
        await message.channel.send('Аыыы.. здарова, {0}, а я Грайнд! {1.author.mention}'.format(reg_search.group(2), message))
    reg_search = re.search(r'average\s(\w*\s)+(enjoyer|fan)', message.content, re.IGNORECASE)
    if reg_search:
        await play_sound(message, 'botenjoyer.mp3')
    reg_search = re.search(r'(\w*\s)+lore', message.content, re.IGNORECASE)
    if reg_search:
        await play_sound(message, 'lore.mp3')
    await bot.process_commands(message)


@bot.command()
async def leave(ctx):
    try:
        await voice_client.disconnect()
        await ctx.send('Э, братан, полегче... Уже выхожу.')
    except AttributeError:
        await ctx.send('АЫыы.. так я же не в войсе, ёпт.')


@bot.command()
async def tts(ctx, *, message):
    global voice_client
    tts = gTTS(message, lang='ru')
    tts.save('tts.mp3')
    await play_sound(ctx, 'tts.mp3')


@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def eko(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} кричит: \"Эко гей!\"')


@bot.command()
async def bulling(ctx):
    author = ctx.message.author
    user = random.choice(ctx.guild.members)
    await ctx.send(f'{author.mention} забуллил {user.mention}!')


@bot.command()
async def raketa(ctx):
    response = requests.get('https://some-random-api.ml/img/raccoon')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=0xff9900, title='РАКЕТА')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)


@bot.command()
async def pat(ctx, target):
    await action(ctx, 0xff3300, target, 'сделал пат пат пат', 'https://some-random-api.ml/animu/pat')


@bot.command()
async def hug(ctx, target):
    await action(ctx, 0x42f560, target, 'обнял', 'https://some-random-api.ml/animu/hug')


@bot.command()
async def wink(ctx, target):
    await action(ctx, 0xd1f542, target, 'подмигнул', 'https://some-random-api.ml/animu/wink')


@bot.command()
async def gayify(ctx, memavatar: discord.Member = None):
    await filter(ctx, 0xff006f, memavatar.avatar_url, 'https://some-random-api.ml/canvas/gay')


@bot.command()
async def sovietify(ctx, memavatar: discord.Member = None):
    await filter(ctx, 0xff0000, memavatar.avatar_url, 'https://some-random-api.ml/canvas/comrade')


bot.run(secret.TOKEN)