from bot.commands.cleverbot import CleverbotCommand
from bot.commands.command import Command
from bot.commands.draw import DrawCommand
from bot.commands.imagemacros import ImageMacroCommand
from bot.commands.lock import LockCommand, UnlockCommand
from bot.commands.mute import MuteCommand
from bot.commands.unmute import UnmuteCommand
from bot.chan_track import muted_chans
import discord
import asyncio
import os

client = discord.Client()
commands = {
    "unmute": UnmuteCommand(),
    "mute": MuteCommand(),
    "çekiliş": DrawCommand(),
    "cleverbot": CleverbotCommand(),
    "i": ImageMacroCommand(),
    "help": Command(),
    "kilitle": LockCommand(),
    "kilitac": UnlockCommand(),
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

    for chan in client.get_all_channels():
        print("#" + chan.name + " okundu.")
        muted_chans[chan.name] = False

    print("Ready! " + client.user.name + " " + client.user.id)


@client.event
async def on_message(message):
    isAuthorAdmin = False
    for role in message.author.roles:
        for check_role in cfg["admin_roles"]:
            if role.name == check_role:
                isAuthorAdmin = True

    if muted_chans[message.channel.name]:
        if not isAuthorAdmin:
            await client.delete_message(message)
            await client.send_message(message.author, "#" + message.channel.name + " şu anda kilitlidir.")
            return

    if message.content.startswith('!'):
        if message.author == client.user:
            return

        cmd = message.content[1:].split()[0]
        c_args = message.content[1:].split()[1:]

        print("Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

        if not commands.get(cmd):
            await client.send_message(message.channel, message.author.mention + " Bu komut yok!")
            return

        if commands[cmd].requiresAdmin():
            if isAuthorAdmin:
                await commands[cmd].do(client, message, c_args, cfg)

                if commands[cmd].deleteCMDMsg():
                    await client.delete_message(message)
            else:
                await client.send_message(message.channel, message.author.mention + " Yetkin yok!")
        else:
            await commands[cmd].do(message, c_args, cfg)

            if commands[cmd].deleteCMDMsg():
                await client.delete_message(message)


def start(config):
    global cfg
    cfg = config

    print("Starting...")
    client.run(config["token"])
    return 0
