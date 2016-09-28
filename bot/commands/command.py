import os

import discord

from bot import config


class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "help"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        from bot.stuff import commands, respond

        img = ""
        for file in os.listdir(cfg["img_dir"]):
            img = img + "  - " + file.split(".")[0] + "\n"

        resp = ""
        for response in respond[message.server.id]:
            resp = resp + "  - " + response + "\n"

        acmd_fnd = False
        cmd = ""
        for command in commands:
            cmd_c = (command[1])()
            if cmd_c.command() != "_____________nonecommandsrsly":
                if cmd_c.requiresAdmin():
                    acmd_fnd = False
                    for role in message.author.roles:
                        if acmd_fnd: break
                        for check_role in config.get_key(message.server.id, "admin_roles"):
                            if role.name == check_role:
                                cmd = cmd + "  - !" + cmd_c.command() + "\n"
                                acmd_fnd = True
                                break
                else:
                    cmd = cmd + "  - !" + cmd_c.command() + "\n"

        await client.send_message(message.author, """```
Bot 1.0.0! ( by @admicos )
Kaynak: https://admicos.cf/s?EayKf
Komutlar:
%s

Resimler:
%s

Bot size cevap da verir! Şu kelimeleri yazdıklarınızda kullanmayı deneyin!:
%s
```""" % (cmd, img, resp))
