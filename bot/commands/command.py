class Command:
    def requiresAdmin(self):
        return False

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, "@" + message.author.name + " Bu komut yapılmadı!")
