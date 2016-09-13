from bot.commands.command import Command
import random


class DrawCommand(Command):
    def requiresAdmin(self):
        return True

    async def do(self, client, message):
        participants = message.channel.server.members
        winner = random.randint(0, len(participants))

        await client.send_message(message.channel, "Kazanan kişi, " + list(message.channel.server.members)[winner].name)
