class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, """```
Bot 1.0.0! ( by @admicos )
Kaynak: https://admicos.cf/s?EayKf
Komutlar:
!cleverbot <mesaj>
!i <resim>
```""")
