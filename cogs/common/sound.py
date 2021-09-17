import discord
import asyncio


async def play_sound(ctx, voice_client, sound: str):
    voice_client = None
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