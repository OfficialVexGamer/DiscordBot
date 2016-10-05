import discord

from bot.commands.command import Command
from bot import sound


class SoundStopCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_stop"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        sound.player[message.server.id].stop()
