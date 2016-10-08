import discord

from bot import config
from bot import i18n
from bot.commands.command import Command


class GetConfCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "getconf"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        if len(args) == 1:
            key_name = args[0]
            key = config.get_key(message.server.id, key_name)
            ret = "\n"
            if key:
                if isinstance(key, list):
                    for k in key:
                        ret += "  - {}\n".format(k)
                else:
                    ret = key

                await client.send_message(message.channel, """```yaml

{}: {}```""".format(key_name, ret))
                return

            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_getconf_help"))
