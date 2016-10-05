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
        if not sound.queue[message.server.id]:
            sound.mk_server_queue(message.server.id)

        while not sound.queue[message.server.id].empty():
            if not sound.player.get(message.server.id):
                await sound.play(message.server.id, client, message, config.get_key(message.server.id, "music_chan"))
            elif sound.player[message.server.id].is_done():
                await sound.play(message.server.id, client, message, config.get_key(message.server.id, "music_chan"))

            await asyncio.sleep(sound.player[message.server.id].duration + 1)