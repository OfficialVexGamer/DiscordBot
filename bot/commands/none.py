from bot import i18n
from bot.commands.command import Command


class NoneCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "_____________nonecommandsrsly"

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, i18n.get_localized_str("bot_nocmd", {"mention":
                                                                                        message.author.mention}))
