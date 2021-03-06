import discord

from bot import config
from bot import i18n
from bot.commands.command import Command


class UnmuteCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "unmute"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_unmute_help"))
            return

        if not config.get_key(message.server.id, "mute_role"):
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "bot_config_error", {"cmd": self.command(),
                                                                                                   "key": "mute_role"}))
            return

        if not config.get_key(message.server.id, "admin_roles"):
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "bot_config_error", {"cmd": self.command(),
                                                                                                   "key": "admin_roles"}))
            return

        nameToMute = " ".join(args)

        for member in message.server.members:
            if nameToMute.lower().strip() == member.name.lower():
                for role in member.roles:
                    for check_role in config.get_key(message.server.id, "admin_roles"):
                        if role.name == check_role:
                            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_mute_admin"))
                            return
                        elif role.name == config.get_key(message.server.id, "mute_role"):
                            await client.remove_roles(member, role)
                            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_unmute", {
                                "mention": member.mention
                            }))
                            return

        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_mute_notfound", {"name": nameToMute}))
