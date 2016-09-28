import discord

from bot.commands.command import Command
from bot import i18n


class NoneCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "_____________nonecommandsrsly"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "bot_nocmd", {"mention":
                                                                                        message.author.mention}))
