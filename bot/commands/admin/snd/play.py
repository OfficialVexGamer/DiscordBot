import asyncio

import discord

from bot.commands.command import Command
from bot import sound
from bot import i18n


class SoundPlayCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        while not sound.queue.empty():
            if not sound.player:
                await sound.play(client, message, config["music_chan"])
            elif sound.player.is_done():
                await sound.play(client, message, config["music_chan"])

            await asyncio.sleep(sound.player.duration + 1)

        await client.change_status(game=discord.Game(name=i18n.get_localized_str("bot_game")))
