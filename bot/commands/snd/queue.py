from bot.commands.command import Command
from bot import sound


class SoundQueueCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_queue"

    async def do(self, client, message, args, config={}):
        sound.add_queue(args[0])