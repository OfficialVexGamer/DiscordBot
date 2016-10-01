import discord

from bot.commands.command import Command
from bot import sound
from bot import i18n


class SoundVolCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_vol"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_volume_help"))
            return

        sound.change_vol(message.server.id, float(args[0]))
