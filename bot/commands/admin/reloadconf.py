import discord

from bot import config
from bot import i18n
from bot.commands.command import Command


class ReloadConfCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "reloadconf"

    def shouldModlog(self):
        return False

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        await client.on_server_join(message.server)
        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_reloadconf"))
