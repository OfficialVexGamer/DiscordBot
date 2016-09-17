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

        voice = await client.join_voice_channel()#abc