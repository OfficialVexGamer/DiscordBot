import asyncio

from bot.commands.command import Command
from bot import sound


class SoundPlayCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    async def do(self, client, message, args, config={}):
        while not sound.queue.empty():
            if not sound.player:
                await sound.play(client, message, config["music_chan"])
                continue

            if sound.player.is_done():
                await sound.play(client, message, config["music_chan"])

            await asyncio.sleep(sound.player.duration + 1)
