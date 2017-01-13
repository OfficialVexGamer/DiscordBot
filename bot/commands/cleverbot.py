import discord


class CleverbotCommand:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "help"

    def shouldModlog(self):
        return False

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        await client.send_message(message.channel, "Cleverbot is disabled. Check back later!")