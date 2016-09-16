from bot.commands.command import Command


class NoneCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "_____________nonecommandsrsly"

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, message.author.mention + " Bu komut yok!")
