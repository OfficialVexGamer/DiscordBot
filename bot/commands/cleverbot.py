import discord

from bot import config
from bot.commands.command import Command
from bot import i18n
from bot.cleverbot import Cleverbot


class CleverbotCommand(Command):
    cb = Cleverbot()

    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "cleverbot"

    def shouldModlog(self):
        return False

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_cleverbot_nothing", {"mention":
                                                                                                        message.author.mention}))
            return

        for chan in config.get_key(message.server.id, "cleverbot_channels"):
            if chan == message.channel.name:
                input = " ".join(args)

                await client.send_message(message.channel,
                                          message.author.mention + ", " +
                                          self.cb.ask(input))
                return

        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_cleverbot_wrongchannel", {"mention":
                                                                                                         message.author.mention}))
