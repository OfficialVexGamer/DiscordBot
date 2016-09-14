from bot.commands.command import Command
import os


class ImageMacroCommand(Command):
    def requiresAdmin(self):
        return False

    async def do(self, client, message, args, config={}):
        if os.path.exists(os.path.join(config["img_dir"], args[0] + ".png")):
            # with open(os.path.join(config["img_dir"], args[0] + ".png"), 'rb') as f:
            #     await client.send_file(message.channel, f)
            #     return
            await client.send_message(message.channel, message.author.mention + " " + config["img_url_prefix"] + args[0] + ".png")
        else:
            await client.send_message(message.channel, message.author.mention + " Bu resim yok!")
