from datetime import timedelta
from bot.commands.command import Command
from bot import i18n
import discord
import time


class StatsCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return False

    def command(self):
        return "stats"

    def shouldModlog(self):
        return False

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        members = 0
        channels = 0
        large_servers = 0

        for server in client.servers:
            members += len(server.members)
            channels += len(server.channels)

            if server.large:
                large_servers += 1

        with open('/proc/uptime', 'r') as f:
            uptime_seconds = round(float(f.readline().split()[0]), 0)
            uptime_string = str(timedelta(seconds=uptime_seconds))

        await client.send_message(message.channel, i18n.get_localized_str(
            message.server.id, "stats", {
                "server_count":  len(client.servers),
                "user_count":    members,
                "channel_count": channels,
                "considered_large": large_servers,
                "uptime": uptime_string,
                "bot_uptime": str(timedelta(seconds=int(time.time() - client.start_time)))
            })
        )
