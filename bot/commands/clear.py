class ClearCommand(Command):
    def requiresAdmin(self):
        return True

    async def do(self, client, message, args, config={}):
        if not config["mute_role"]:
            await client.send_message(message.channel, """```
            .


















































































































































































































            ```""" + message.author.mention + " chati temizledi.")
            return