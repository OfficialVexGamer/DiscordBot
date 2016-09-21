from bot.commands.command import Command


class ClearCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "clear"

    async def do(self, client, message, args, config={}):
        text = """. """
        for i in range(100):
            text = text + """

             """
        await client.send_message(message.channel, text + "\n" + message.author.mention + " chati temizledi.")
        return