from bot.commands.command import Command
from bot import sound
from bot import i18n


class SoundChanCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "snd_aktif"

    async def do(self, client, message, args, config={}):
        if sound.voice:
            await client.send_message(message.channel, i18n.get_localized_str("cmd_snd_init"))
            return

        for channel in message.server.channels:
            if channel.name == config["voice_chan"]:
                sound.voice = await client.join_voice_channel(channel)
                await client.send_message(message.channel, i18n.get_localized_str("cmd_snd_init_ok", {"mention":
                                                                                                      message.author.mention}))
                break
