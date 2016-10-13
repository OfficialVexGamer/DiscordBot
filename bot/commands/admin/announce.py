import discord

from bot.commands.command import Command


class AnnounceCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "announce"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        for channel in message.server.channels:
            if channel.type == discord.ChannelType.text:
                await client.send_message(channel, " ".join(args))
