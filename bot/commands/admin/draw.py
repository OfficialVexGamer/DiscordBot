import discord

from bot import i18n
from bot.commands.command import Command
import random


class DrawCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "raffle"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        while True:
            participants = message.server.members
            winner = random.randint(0, len(participants) - 1)

            if list(participants)[winner].name != client.user.name:
                await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_draw", {"winner":
                                                                                               list(participants)[winner].name}))
                break
