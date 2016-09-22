from bot import i18n
from bot.commands.command import Command
from bot.cleverbot import Cleverbot


class CleverbotCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "cleverbot"

    async def do(self, client, message, args, config={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str("cmd_cleverbot_nothing", {"mention":
                                                                                                        message.author.mention}))
            return

        for chan in config["cleverbot_channels"]:
            if chan == message.channel.name:
                input = args[0]

                for i in range(1, len(args)):
                    input = input + " " + args[i]

                cb = Cleverbot()

                await client.send_message(message.channel, message.author.mention + ", " + cb.ask(input)) #+ " özür dilerim canım cicim tatlım"))
                return

        await client.send_message(message.channel, i18n.get_localized_str("cmd_cleverbot_wrongchannel", {"mention":
                                                                                                         message.author.mention}))
