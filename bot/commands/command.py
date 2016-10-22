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

    def help(self, server_id: str):
        _hlp = i18n.get_localized_str(server_id, "help_" + self.command())
        if _hlp == "STRING NOT FOUND: help_" + self.command():
            return "```" + config.get_key(server_id, "cmd_prefix") + \
            self.command() + " " + i18n.get_localized_str(
                server_id, "help_notfound"
            ) + "```"

        return "```" + config.get_key(server_id, "cmd_prefix") + \
               self.command() + " " + _hlp + "```"

    def _command_is_disabled(self, server: str, cmd: str):
        for dcmd in config.get_key(server, "disabled_commands"):
            if cmd == dcmd:
                return True
        return False

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        from bot.stuff import commands, bot_version, find_cmd_class

        if len(args) >= 1:
            _cmd = find_cmd_class(args[0])
            if _cmd.command() != "_____________nonecommandsrsly":
                await client.send_message(message.author, _cmd.help(message.server.id))

            return

        cmd = ""
        for command in commands:
            cmd_c = (command[1])()
            if cmd_c.command() != "_____________nonecommandsrsly":
                if not self._command_is_disabled(message.server.id, cmd_c.command()):
                    if cmd_c.requiresAdmin():
                        acmd_fnd = False
                        if message.author.permissions_in(message.channel).administrator:
                            cmd = cmd + "  - " + config.get_key(message.server.id, "cmd_prefix") + cmd_c.command() + "\n"
                        else:
                            for role in message.author.roles:
                                if acmd_fnd: break
                                for check_role in config.get_key(message.server.id, "admin_roles"):
                                    if role.name == check_role:
                                        cmd = cmd + "  - " + config.get_key(message.server.id, "cmd_prefix") \
                                              + cmd_c.command() + "\n"
                                        acmd_fnd = True
                                        break
                    else:
                        cmd = cmd + "  - " + config.get_key(message.server.id, "cmd_prefix") + cmd_c.command() + "\n"

        await client.send_message(message.author, i18n.get_localized_str(message.server.id, "help", {
            "commands": cmd,
            "version": bot_version,
        }))
