from bot.commands.command import Command
from bot.cleverbot import Cleverbot


class CleverbotCommand(Command):
    def requiresAdmin(self):
        return False

    async def do(self, client, message, args, config={}):
        for chan in config["cleverbot_channels"]:
            if chan == message.channel.name:
                input = args[0]

                for i in range(1, len(args)):
                    input = input + " " + args[i]

                cb = Cleverbot()

                await client.send_message(message.channel, message.author.mention + ", " + cb.ask(input))
                return

        await client.send_message(message.channel, "@" + message.author.name +
                                  " Cleverbot belirli kanallar dışında kullanılamaz!")
