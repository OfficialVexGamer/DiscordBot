from bot.commands.command import Command
from bot import stuff


class SoundPlayCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    def get_snd_mins(self, in_secs):
        m, s = divmod(in_secs, 60)
        h, m = divmod(m, 60)

        return "%s:%s:%s" % (h, m, s)

    async def do(self, client, message, args, config={}):
        player = await stuff.voice.create_ytdl_player(args[0])  # TEST URL
        await client.send_message(message.channel, """```""" + player.name + """
by """ + player.uploader + """ (""" + self.get_snd_mins(player.duration) + """)```""")
        player.start()
