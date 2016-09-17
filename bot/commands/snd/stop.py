from bot.commands.command import Command
from bot import sound


class SoundStopCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_stop"

    async def do(self, client, message, args, config={}):
        sound.clear_queue()