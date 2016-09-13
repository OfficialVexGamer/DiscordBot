from bot.commands.mute import MuteCommand
import discord
import asyncio

client = discord.Client()
commands = {
    "mute": MuteCommand()
}


@client.event
async def on_ready():
    print("[OK] Ready! " + client.user.name + " " + client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.author == client.user:
            return

        cmd = message.content[1:].split()[0]
        c_args = message.content[1:].split()[1:]

        print("[OK] Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

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
            commands[cmd].do(client, message, c_args, cfg)
            return

        await client.send_message(message.channel, "@" + message.author.name + " Yetkin yok!")


def start(config):
    global cfg
    cfg = config

    print("[OK] Starting...")
    client.run(config["token"])
    return 0
