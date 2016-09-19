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
        if len(args) < 1:
            await client.send_message(message.channel, "!snd_queue <url>")
            return

        sound.add_queue(args[0])
        await client.send_message(message.channel, "Bir şarkı listeye eklendi! (listede %i inci)" % sound.queue.qsize())
