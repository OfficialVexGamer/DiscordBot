import discord

from bot import config
from bot import i18n
from bot.commands.command import Command


class ConfCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "conf"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        if len(args) > 1:
            config.set_key(message.server.id, args.pop(), " ".join(args))
            await client.on_server_join(message.server)
            return

        client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_conf_help"))