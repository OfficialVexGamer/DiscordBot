from bot.commands.clear import ClearCommand
from bot.commands.cleverbot import CleverbotCommand
from bot.commands.command import Command
from bot.commands.draw import DrawCommand
from bot.commands.imagemacros import ImageMacroCommand
from bot.commands.lock import LockCommand, UnlockCommand
from bot.commands.mute import MuteCommand
from bot.commands.unmute import UnmuteCommand
from bot.chan_track import muted_chans, server, msgChan
import discord
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
    "clear": ClearCommand(),
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
        muted_chans[chan.name] = False

    global server
    server = client.get_server(0)

    print("Ready! " + client.user.name + " " + client.user.id)


@client.event
def on_channel_delete(channel):
    muted_chans[channel.name] = None


@client.event
def on_channel_create(channel):
    muted_chans[channel.name] = False


@client.event
async def on_message(message):
    isAuthorAdmin = False
    if type(message.author) == discord.User:  # PM
        if message.author.name == "admicos" and str(message.author.discriminator) == "5389":
            global msgChan

            if message.content.startswith('!id '):
                msgChan = str(message.content[4:])
            elif message.content.startswith("!name "):
                await client.edit_profile(username=str(message.content[6:]))
            else:
                await client.send_message(client.get_channel(msgChan), message.content)

        return

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
            await commands[cmd].do(client, message, c_args, cfg)

            if commands[cmd].deleteCMDMsg():
                await client.delete_message(message)


def start(config):
    global cfg
    cfg = config

    print("Starting...")
    client.run(config["token"])
    return 0
