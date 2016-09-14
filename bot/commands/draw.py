from bot.commands.command import Command
import random


class DrawCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    async def do(self, client, message, args, config={}):
        while True:
            participants = message.channel.server.members
            winner = random.randint(0, len(participants) - 1)

            if list(participants)[winner].name != client.user.name:
                await client.send_message(message.channel, "Kazanan kişi, " + list(participants)[winner].name)
                break
