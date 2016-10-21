from bot import i18n
from bot.commands.command import Command
import discord
import markovify


class MarkovCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "markov"

    async def do(self, client: discord.Client, message: discord.Message, args: list, cfg={}):
        text = ""
        ret = ""

        async for msg in client.logs_from(message.channel, limit=500):
            text += msg.content + "\n"

        text_model = markovify.Text(text)
        ret = text_model.make_sentence(
            tries=100, max_overlap_ratio=2147483647,
            max_overlap_total=2147483647)

        if ret is None:
            ret = i18n.get_localized_str(message.server.id,
                                         "cmd_markov_not_enough_msg")
        else:
            print("Generated markov chain: " + ret)

        await client.send_message(message.channel, ret)
