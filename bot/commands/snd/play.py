import asyncio

from bot.commands.command import Command
from bot import sound


class SoundPlayCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_play"

    async def do(self, client, message, args, config={}):
        while not sound.queue.empty():
            if not sound.player:
                sound.player = await sound.voice.create_ytdl_player(sound.queue.get())
                await client.send_message(message.channel, """```""" + sound.player.title + """
by """ + sound.player.uploader + """ (""" + sound.get_snd_mins(sound.player.duration) + """)```""")
                sound.player.start()
                continue

            if sound.player.is_done():
                sound.player = await sound.voice.create_ytdl_player(sound.queue.get())
                await client.send_message(message.channel, """```""" + sound.player.title + """
by """ + sound.player.uploader + """ (""" + sound.get_snd_mins(sound.player.duration) + """)```""")
                sound.player.start()

            await asyncio.sleep(sound.player.duration + 1)
