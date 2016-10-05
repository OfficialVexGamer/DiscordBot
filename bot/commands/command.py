from bot import config
from bot import i18n
import discord


class Command:
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "help"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        from bot.stuff import commands, bot_version

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
                                cmd = cmd + "  - " + config.get_key(message.server.id, "cmd_prefix") + cmd_c.command() \
                                          + "\n"
                                acmd_fnd = True
                                break
                else:
                    cmd = cmd + "  - " + config.get_key(message.server.id, "cmd_prefix") + cmd_c.command() + "\n"

        await client.send_message(message.author, i18n.get_localized_str(message.server.id, "help", {
            "commands": cmd,
            "version": bot_version,
        }))
