from bot.chan_track import muted_chans
from bot.commands.command import Command


class LockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, message.author.mention + " Kanalı kilitledi.")
        muted_chans[message.channel.name] = True


class UnlockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    async def do(self, client, message, args, config={}):
        muted_chans[message.channel.name] = False
        await client.send_message(message.channel, message.author.mention + " Kanal kilidini açtı.")
