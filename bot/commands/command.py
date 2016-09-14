class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, "Bot 1.0.0! ( by @admicos )")
        await client.send_message(message.channel, "Kaynak: admicos.cf/s?EayKf")
        await client.send_message(message.channel, "Komutlar: ")
        await client.send_message(message.channel, "!cleverbot <mesaj>")
        await client.send_message(message.channel, "!i <resim>")
