import random
import discord
from discord.ext import commands


class Utilities(commands.Cog):

    def __init__(self, client):
        print("Loaded utilities cog")
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Понг! Мой пинг {round(self.client.latency * 1000)}мс")

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command()
    async def change_activity(self, ctx):
        activities = [
            discord.Activity(type=discord.ActivityType.watching, name="на твою морду"),
            discord.Activity(type=discord.ActivityType.listening, name="твой голос"),
            discord.Activity(type=discord.ActivityType.playing, name="ящик")
        ]
        await self.client.change_presence(activity=random.choice(activities))


def setup(client):
    client.add_cog(Utilities(client))