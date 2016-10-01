import discord

from bot import i18n
from bot.commands.command import Command
from bot import sound


class SoundQueueCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_queue"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_queue_help"))
            return

        sound.add_queue(message.server.id, args[0])

        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_queue", {"index":
                                                                                            sound.queue.qsize()}))
