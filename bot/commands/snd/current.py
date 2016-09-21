from bot.commands.command import Command
from bot import sound


class CurrentMusicCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_suanki"

    async def do(self, client, message, args, config={}):
        if not sound.player:
            await client.send_message(message.channel, message.author.mention + " Şu anda hiç bir şey çalmıyor.")
            return

        await client.send_message(message.channel, message.author.mention + """```Ad: """ + sound.player.title + """
Yapımcı: """ + sound.player.uploader + """
Zaman: """ + sound.get_snd_mins(sound.player.duration) + """)
URL: """ + sound.player.url + """```""")
