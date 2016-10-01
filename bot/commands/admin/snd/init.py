import discord

from bot import config
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

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        if sound.voice.get(message.server.id):
            await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_init"))
            return

        for channel in message.server.channels:
            if channel.name == config.get_key(message.server.id, "voice_chan"):
                sound.voice[message.server.id] = await client.join_voice_channel(channel)
                sound.mk_server_queue(message.server.id)
                await client.send_message(message.channel, i18n.get_localized_str(message.server.id, "cmd_snd_init_ok", {
                    "mention": message.author.mention
                }))
                break
