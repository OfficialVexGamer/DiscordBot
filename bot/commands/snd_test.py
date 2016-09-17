from bot.commands.command import Command
from bot import stuff


class SoundTestCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    async def do(self, client, message, args, config={}):
        player = await stuff.voice.create_ytdl_player(args[0])  # TEST URL
        player.start()
