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
        if not args[0]:
            await client.send_message(message.channel, "!snd_queue <url>")
            return

        sound.add_queue(args[0])
        client.send_message(message.channel, args[0] + " listeye eklendi!")
