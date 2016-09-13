from bot.commands.test import TestCommand
import discord
import asyncio

client = discord.Client()
commands = {
    "test": TestCommand()
}


@client.event
async def on_ready():
    print("[OK] Ready! " + client.user.name + " " + client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.author == client.user:
            return

        print("[OK] Komut: (" + message.author.name + ") " + message.content[1:])

        if not commands.get(message.content[1:]):
            await client.send_message(message.channel, "@" + message.author.name + " Bu komut yok!")
            return

        if commands[message.content[1:]].requiresAdmin():
            for role in message.author.roles:
                for check_role in cfg["admin_roles"]:
                    if role.name == check_role:
                        await commands[message.content[1:]].do(client, message)
                        return
        else:
            commands[message.content[1:]].do(client, message)
            return

        await client.send_message(message.channel, "@" + message.author.name + " Yetkin yok!")


def start(config):
    global cfg
    cfg = config

    print("[OK] Starting...")
    client.run(config["token"])
    return 0
