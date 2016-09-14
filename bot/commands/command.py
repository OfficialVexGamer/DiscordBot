import os


class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    async def do(self, client, message, args, config={}):
        fs = ""
        for file in os.listdir(config["img_dir"]):
            fs = fs + " - " + file.split(".")[0] + "\n"

        await client.send_message(message.channel, """```
Bot 1.0.0! ( by @admicos )
Kaynak: https://admicos.cf/s?EayKf
Komutlar:
  - !cleverbot <mesaj>
  - !i <resim>

Resimler:
%s
```""" % fs)
