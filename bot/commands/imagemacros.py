from bot.commands.command import Command
from bot import i18n
import os


class ImageMacroCommand(Command):
    def requiresAdmin(self):
        return False

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "i"

    async def do(self, client, message, args, config={}):
        if len(args) < 1:
            await client.send_message(message.channel, i18n.get_localized_str("cmd_i_help", {"mention":
                                                                                             message.author.mention}))
            return

        if os.path.exists(os.path.join(config["img_dir"], args[0] + ".png")):
            # with open(os.path.join(config["img_dir"], args[0] + ".png"), 'rb') as f:
            #     await client.send_file(message.channel, f)
            #     return
            await client.send_message(message.channel, message.author.mention + " " + config["img_url_prefix"] + args[0] + ".png")
        else:
            await client.send_message(message.channel, i18n.get_localized_str("cmd_i_notfound", {"mention":
                                                                                                 message.author.mention}))
