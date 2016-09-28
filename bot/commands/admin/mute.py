import discord

from bot import i18n
from bot.commands.command import Command


class MuteCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "mute"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str("cmd_mute_help"))
            return

        if not config["mute_role"]:
            await client.send_message(message.channel, i18n.get_localized_str("bot_config_error", {"cmd": self.command(),
                                                                                                   "key": "mute_role"}))
            return

        if not config["admin_roles"]:
            await client.send_message(message.channel, i18n.get_localized_str("bot_config_error", {"cmd": self.command(),
                                                                                                   "key": "admin_roles"}))
            return

        nameToMute = ""
        for arg in args:
            nameToMute = nameToMute + " " + arg

        for member in message.channel.server.members:
            if nameToMute.lower().strip() == member.name.lower():
                for role in member.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            await client.send_message(message.channel, i18n.get_localized_str("cmd_mute_admin"))
                            return

                for role in message.server.roles:
                    if role.name.lower() == config["mute_role"].lower():
                        await client.add_roles(member, role)
                        await client.send_message(message.channel, i18n.get_localized_str("cmd_mute", {"mention":
                                                                                                       member.mention}))
                        return

                await client.send_message(message.channel, i18n.get_localized_str("bot_serv_cfg_error", {
                    "cmd": self.command(),
                    "err": i18n.get_localized_str("err_nomuterole")
                }))
                return

        await client.send_message(message.channel, i18n.get_localized_str("cmd_mute_notfound", {"name": nameToMute}))
