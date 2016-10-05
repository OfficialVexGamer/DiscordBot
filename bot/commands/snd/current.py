import discord

from bot.commands.command import Command
from bot import i18n
from bot import sound


class CurrentMusicCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_current"

    async def do(self, client: discord.Client, message: discord.Message, args: list, config={}):
        if not sound.player:
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_current_npy"))
            return

        await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "sound_playing_template", {
            "sound": sound.player[message.server.id],
            "duration": sound.get_snd_mins(sound.player[message.server.id].duration)
        }))
