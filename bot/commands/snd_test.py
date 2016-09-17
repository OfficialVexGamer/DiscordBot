from bot.commands.command import Command


class SoundTestCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_test"

    async def do(self, client, message, args, config={}):
        import discord
        if not discord.opus.is_loaded():
            # the 'opus' library here is opus.dll on windows
            # or libopus.so on linux in the current directory
            # you should replace this with the location the
            # opus library is located in and with the proper filename.
            # note that on windows this DLL is automatically provided for you
            discord.opus.load_opus('opus')

        voice = None
        for channel in message.server.channels:
            if channel.name == config["voice_chan"]:
                voice = await client.join_voice_channel(channel)
                break

        if not voice:
            await client.send_message(message.channel, message.author.mention + "Ses kanalı " +
                                      config["voice_chan"] + " bulunamadı")
            return

        player = voice.create_ytdl_player('https://www.youtube.com/watch?v=NF26ZyZRJbU')  # TEST URL
        player.start()
