from bot import stuff
from bot.commands.command import Command


class LockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "kilitle"

    async def do(self, client, message, args, config={}):
        await client.send_message(message.channel, message.author.mention + " Kanalı kilitledi.")
        stuff.muted_chans[message.channel.name] = True


class UnlockCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "kilitaç"

    async def do(self, client, message, args, config={}):
        stuff.muted_chans[message.channel.name] = False
        await client.send_message(message.channel, message.author.mention + " Kanal kilidini açtı.")