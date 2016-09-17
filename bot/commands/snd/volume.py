from bot.commands.command import Command
from bot import sound


class SoundVolCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_vol"

    async def do(self, client, message, args, config={}):
        if not sound.player:
            await client.send_message(message.channel, message.author.mention +
                                      " Lütfen önce !snd_play ile bir müzik açın!")

        sound.change_vol(float(args[0]))
