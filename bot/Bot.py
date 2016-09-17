from bot.stuff import muted_chans, server, msgChan, respond, find_cmd_class
import discord
import os

client = discord.Client()


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
async def on_channel_delete(channel):
    muted_chans[channel.name] = None


@client.event
async def on_channel_create(channel):
    muted_chans[channel.name] = False


@client.event
async def on_message(message):
    isAuthorAdmin = False
    if type(message.author) == discord.User:  # PM
        if message.author.name == cfg["speak_person"]["name"] and str(message.author.discriminator) == str(cfg["speak_person"]["iden"]):
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
        cmd_class = find_cmd_class(cmd)

        print("Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

        if cmd_class.requiresAdmin():
            if isAuthorAdmin:
                await cmd_class.do(client, message, c_args, cfg)

                if cmd_class.deleteCMDMsg():
                    await client.delete_message(message)
            else:
                await client.send_message(message.channel, message.author.mention + " Yetkin yok!")
        else:
            await cmd_class.do(client, message, c_args, cfg)

            if cmd_class.deleteCMDMsg():
                await client.delete_message(message)
    else:
        wc = 0
        for word in message.content.lower().split():
            if wc < 5:
                wc += 1
                if respond.get(word):
                    await client.send_message(message.channel, message.author.mention + " " + respond.get(word))


def start(config):
    global cfg
    cfg = config

    print("Starting...")
    client.run(config["token"])
    return 0
