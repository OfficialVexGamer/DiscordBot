import discord

from bot.commands.command import Command
from bot import i18n


class StatsCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "stats"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        members = 0
        channels = 0
        large_servers = 0

        for server in client.servers:
            members += len(server.members)
            channels += len(server.channels)

            if server.large:
                large_servers += 1

        await client.send_message(message.channel, i18n.get_localized_str(
            message.server.id, "stats", {
                "server_count":  len(client.servers),
                "user_count":    members,
                "channel_count": channels,
                "considered_large": large_servers
            })
        )
