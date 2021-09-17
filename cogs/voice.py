from gtts import gTTS
import re
from cogs.common import sound as play
from discord.ext import commands


class Voice(commands.Cog):

    def __init__(self, client):
        print("Loaded voice cog")
        self.client = client
        global voice_client
        voice_client = None

    @commands.command()
    async def leave(self, ctx):
        global voice_client
        if(voice_client):
            try:
                await voice_client.disconnect()
                await ctx.send('Э, братан, полегче... Уже выхожу.')
            except AttributeError:
                await ctx.send('АЫыы.. так я же не в войсе, ёпт.')

    @commands.command()
    async def tts(self, ctx, *, message):
        global voice_client
        tts = gTTS(message, lang='ru')
        tts.save('tts.mp3')
        await play.play_sound(ctx, voice_client, 'tts.mp3')

    @commands.Cog.listener()
    async def on_message(self, message):
        global voice_client
        if message.author.id == self.client.user.id:
            return
        reg_search = re.search(r'average\s(\w*\s)+(enjoyer|fan)', message.content, re.IGNORECASE)
        if reg_search:
            await play.play_sound(message, voice_client, 'botenjoyer.mp3')
        reg_search = re.search(r'(\w*\s)+lore', message.content, re.IGNORECASE)
        if reg_search:
            await play.play_sound(message, voice_client, 'lore.mp3')
        #await self.client.process_commands(message)


def setup(client):
    client.add_cog(Voice(client))