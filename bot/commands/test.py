from bot.commands.command import Command


class TestCommand(Command):
    def requiresAdmin(self):
        return True

    async def do(self, client, message):
        await client.send_message(message.channel, message.author.name + ": " + message.content[1:])