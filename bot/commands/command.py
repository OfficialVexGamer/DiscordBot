import os


class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    async def do(self, client, message, args, config={}):
        from bot.stuff import commands, respond

        img = ""
        for file in os.listdir(config["img_dir"]):
            img = img + "  - " + file.split(".")[0] + "\n"

        resp = ""
        for response in respond:
            resp = resp + "  - " + response + "\n"

        cmd = ""
        for comm in commands:
            if commands[comm].requiresAdmin():
                for role in message.author.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            cmd = cmd + "  - !" + comm + "\n"
            else:
                cmd = cmd + "  - !" + comm + "\n"

        await client.send_message(message.author, """```
Bot 1.0.0! ( by @admicos )
Kaynak: https://admicos.cf/s?EayKf
Komutlar:
%s

Resimler:
%s

Bot size cevap ta verir! Şu kelimeleri yazdıklarınızda kullanmayı deneyin!:
%s
```""" % (cmd, img, resp))
