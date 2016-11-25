import discord

from bot import i18n
from bot import stuff
from bot.commands.command import Command


class LockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "lock"

    def shouldModlog(self):
        return True

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}) -> str:
        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_lock", {"mention":
                                                                                       message.author.mention}))
        stuff.muted_chans[message.server.id][message.channel.name] = True


class UnlockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "unlock"

    def shouldModlog(self):
        return True

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        stuff.muted_chans[message.server.id][message.channel.name] = False
        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_unlock", {"mention":
                                                                                         message.author.mention}))