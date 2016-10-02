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
            key_name = args.pop(0)
            key = config.get_key(message.server.id, key_name)
            if key:
                val = " ".join(args)

                if isinstance(key, dict):
                    config.set_key(message.server.id, key_name, val.split(","))
                    await client.on_server_join(message.server)
                    return

                config.set_key(message.server.id, key_name, val)
            client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_conf_nokey", {
                "key": key_name
            }))
            return

        client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_conf_help"))
