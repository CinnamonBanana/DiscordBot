import discord
from discord.ext import commands


class Helpful(commands.Cog):

    def __init__(self, client):
        print("Loaded help cog")
        self.client = client
        client.remove_command("help")

    async def helpcommand(self, ctx, title, descr, syntax):
        em = discord.Embed(title=title, description=descr, color=0xffff00)
        em.add_field(name='~Syntax~', value=syntax)
        await ctx.send(embed=em)

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title=':question: Help',
                           description='Используй &help <команда> для более подробной информации',
                           color=0xffff00)
        em.add_field(name=':microphone2: Voice', value='tts, leave')
        em.add_field(name=':partying_face: Fun', value='bulling, eko,\ngayify, sovietify,\nraketa, wink,\npat, hug')
        em.add_field(name=':gear: Utils', value='echo')
        await ctx.send(embed=em)

    @help.command()
    async def echo(self, ctx):
        await self.helpcommand(ctx, ':speaking_head: Echo', 'АУ.....Ау.....ау.....', '&echo <сообщение>')

    @help.command()
    async def bulling(self, ctx):
        await self.helpcommand(ctx, ':fist: Bulling', 'Буллит случайного пользователя с сервера.', '&bulling')

    @help.command()
    async def eko(self, ctx):
        await self.helpcommand(ctx, ':sob: Eko', 'Классический буллинг эко.', '&eko')

    @help.command()
    async def gayify(self, ctx):
        await self.helpcommand(ctx, ':rainbow_flag: Gayify', 'Make them gay.', '&gayify <@пользователь>')

    @help.command()
    async def sovietify(self, ctx):
        await self.helpcommand(ctx, ':hammer_pick: Sovietify', 'СОЮЮЮЮЮЮЮЗ НЕРУШИИИИМЫЙ РЕСПУБЛИК СВОБОДНЫХ...',
                          '&sovietify <@пользователь>')

    @help.command()
    async def raketa(self, ctx):
        await self.helpcommand(ctx, ':raccoon: Raketa', 'Твой батя начальник туалета.', '&raketa')

    @help.command()
    async def wink(self, ctx):
        await self.helpcommand(ctx, ':wink: Wink', 'Подмигни.', '&wink <@пользователь>')

    @help.command()
    async def pat(self, ctx):
        await self.helpcommand(ctx, ':relieved: Pat', '*pat pat pat pat pat*.', '&pat <@пользователь>')

    @help.command()
    async def hug(self, ctx):
        await self.helpcommand(ctx, ':people_hugging: Hug', 'Обнимааашки.', '&hug <@пользователь>')

    @help.command()
    async def tts(self, ctx):
        await self.helpcommand(ctx, ':speaking_head: TTS', 'Заставь его говорить.', '&tts <сообщение>')

    @help.command()
    async def leave(self, ctx):
        await self.helpcommand(ctx, ':no_entry: Leave', 'А ну пшёл вон.', '&leave')


def setup(client):
    client.add_cog(Helpful(client))