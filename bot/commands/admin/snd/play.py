from bot import config
from bot.commands.command import Command
from bot import sound
from bot import i18n
import asyncio
import discord


class SoundPlayCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        while not sound.queue.empty():
            if not sound.player:
                await sound.play(message.server.id, client, message, config.get_key(message.server.id, "music_chan"))
            elif sound.player.is_done():
                await sound.play(message.server.id, client, message, config.get_key(message.server.id, "music_chan"))

            await asyncio.sleep(sound.player.duration + 1)