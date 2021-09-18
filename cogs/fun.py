import discord
import random
import re
import json
import requests
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        print("***Loaded fun cog")
        self.client = client

    async def filter(self, ctx, embedColor, memavatar, url):
        embed = discord.Embed(color=embedColor)
        parts = str(memavatar).rsplit('?', 2)
        embed.set_image(url=f'{url}?avatar={parts[0]}')
        await ctx.send(embed=embed)

    async def action(self, ctx, embedColor, target, text, url):
        author = ctx.message.author
        response = requests.get(url)
        await ctx.send(f'{author} {text} {target}')
        json_data = json.loads(response.text)
        embed = discord.Embed(color=embedColor)
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def eko(self, ctx):
        author = ctx.message.author
        await ctx.send(f'{author.mention} кричит: \"Эко гей!\"')

    @commands.command()
    async def bulling(self, ctx):
        author = ctx.message.author
        user = random.choice(ctx.guild.members)
        await ctx.send(f'{author.mention} забуллил {user.mention}!')

    @commands.command()
    async def raketa(self, ctx):
        response = requests.get('https://some-random-api.ml/img/raccoon')
        json_data = json.loads(response.text)
        embed = discord.Embed(color=0xff9900, title='РАКЕТА')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, target):
        await self.action(ctx, 0xff3300, target, 'сделал пат пат пат', 'https://some-random-api.ml/animu/pat')

    @commands.command()
    async def hug(self, ctx, target):
        await self.action(ctx, 0x42f560, target, 'обнял', 'https://some-random-api.ml/animu/hug')

    @commands.command()
    async def wink(self, ctx, target):
        await self.action(ctx, 0xd1f542, target, 'подмигнул', 'https://some-random-api.ml/animu/wink')

    @commands.command()
    async def gayify(self, ctx, memavatar: discord.Member = None):
        await self.filter(ctx, 0xff006f, memavatar.avatar_url, 'https://some-random-api.ml/canvas/gay')

    @commands.command()
    async def sovietify(self, ctx, memavatar: discord.Member = None):
        await self.filter(ctx, 0xff0000, memavatar.avatar_url, 'https://some-random-api.ml/canvas/comrade')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        reg_search = re.search(r'(i\'m|im|i am|я) (.{1,})$', message.content, re.IGNORECASE)
        if reg_search:
            await message.channel.send(
                'Аыыы.. здарова, {0}, а я Грайнд! {1.author.mention}'.format(reg_search.group(2), message))


def setup(client):
    client.add_cog(Fun(client))