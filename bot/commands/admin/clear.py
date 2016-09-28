import discord

from bot import i18n
from bot.commands.command import Command


class ClearCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "clear"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        text = """. """
        for i in range(100):
            text = text + """

             """
        await client.send_message(message.channel, text + "\n" + i18n.get_localized_str("cmd_clear", {"mention":
                                                                                                      message.author.mention}))
        return