from bot.commands.command import Command
from bot import stuff


class SoundVolCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_vol"

    def get_snd_mins(self, in_secs):
        m, s = divmod(in_secs, 60)
        h, m = divmod(m, 60)

        return "%s:%s:%s" % (h, m, s)

    async def do(self, client, message, args, config={}):
        if not stuff.player:
            await client.send_message(message.channel, message.author.mention +
                                      " Lütfen önce !snd_play ile bir müzik açın!")

        stuff.player.volume = float(args[0])
        stuff.old_vol = float(args[0])
