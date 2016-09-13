from bot.commands.cleverbot import CleverbotCommand
from bot.commands.draw import DrawCommand
from bot.commands.mute import MuteCommand
from bot.commands.unmute import UnmuteCommand
import discord
import asyncio
import os

client = discord.Client()
commands = {
    "unmute": UnmuteCommand(),
    "mute": MuteCommand(),
    "çekiliş": DrawCommand(),
    "cleverbot": CleverbotCommand()
}


@client.event
async def on_ready():
    if not os.path.exists(".avatar_uploaded"):
        with open(cfg["avatar"], 'rb') as f:
            print("Uploading avatar...")
            await client.edit_profile(avatar=f.read())
            with open(".avatar_uploaded", 'w') as f2:
                f2.write(".")
    else:
        print("Avatar already uploaded (wanna change? remove .avatar_uploaded)")

    print("Ready! " + client.user.name + " " + client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.author == client.user:
            return

        cmd = message.content[1:].split()[0]
        c_args = message.content[1:].split()[1:]

        print("Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

        if not commands.get(cmd):
            await client.send_message(message.channel, "@" + message.author.name + " Bu komut yok!")
            return

        if commands[cmd].requiresAdmin():
            for role in message.author.roles:
                for check_role in cfg["admin_roles"]:
                    if role.name == check_role:
                        await commands[cmd].do(client, message, c_args, cfg)
                        return
        else:
            await commands[cmd].do(client, message, c_args, cfg)
            return

        await client.send_message(message.channel, "@" + message.author.name + " Yetkin yok!")


def start(config):
    global cfg
    cfg = config

    print("Starting...")
    client.run(config["token"])
    return 0
