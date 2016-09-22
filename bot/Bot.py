import sys

from bot import stuff
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
        stuff.muted_chans[chan.name] = False

    global server
    server = list(client.servers)[0]

    await client.change_status(game=discord.Game(name='yardım için !help'))

    print("Ready! " + client.user.name + " " + client.user.id)
    await client.send_message(server, "Bot aktif! (Yardım için !help)")


@client.event
async def on_channel_delete(channel):
    stuff.muted_chans[channel.name] = None


@client.event
async def on_channel_create(channel):
    stuff.muted_chans[channel.name] = False


@client.event
async def on_error(event, *args, **kwargs):
    import traceback
    for server in client.servers:
        for member in server.members:
            if member.name == cfg["speak_person"]["name"] and str(member.discriminator) == str(cfg["speak_person"]["iden"]):
                await client.send_message(member, """```python

###################################
# Something happened to your bot!
# At event: %s
# Args: %s, %s
###################################

%s```""" % (event, str(args), str(kwargs), traceback.format_exc()))
                return
    print("""###################################
# Something happened to your bot!
# Admin not available at server, so i am printing this to the console.
# At event: %s
# Args: %s, %s
###################################

%s""" % (event, str(args), str(kwargs), traceback.format_exc()), file=sys.stderr)


@client.event
async def on_message(message):
    isAuthorAdmin = False
    if type(message.author) == discord.User:  # PM
        if message.author.name == cfg["speak_person"]["name"] and str(message.author.discriminator) == str(cfg["speak_person"]["iden"]):
            if message.content.startswith('!id '):
                stuff.msgChan = str(message.content[4:])
            elif message.content.startswith("!name "):
                await client.edit_profile(username=str(message.content[6:]))
            else:
                await client.send_message(client.get_channel(stuff.msgChan), message.content)

        return

    for role in message.author.roles:
        for check_role in cfg["admin_roles"]:
            if role.name == check_role:
                isAuthorAdmin = True

    if stuff.muted_chans[message.channel.name]:
        if not isAuthorAdmin:
            await client.delete_message(message)
            await client.send_message(message.author, "#" + message.channel.name + " şu anda kilitlidir.")
            return

    if stuff.timeout.get(message.author.name) and stuff.timeout.get(message.author.name) >= 10:
        stuff.remove_timeout_from(message.author.name)
        return
    else:
        stuff.remove_timeouts_except(message.author.name)

    if message.content.startswith('!'):
        if message.author == client.user:
            return

        cmd = message.content[1:].split()[0]
        c_args = message.content[1:].split()[1:]
        cmd_class = stuff.find_cmd_class(cmd)

        print("Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

        if cmd_class.requiresAdmin():
            if isAuthorAdmin:
                await cmd_class.do(client, message, c_args, cfg)
                for chan in client.get_all_channels():
                    if chan.name == cfg["modlog_chan"]:
                        arg_str = ""
                        for arg in c_args:
                            arg_str = arg_str + " " + arg

                        await client.send_message(chan, "{mod}: {cmd} {args}".format({
                            "mod": message.author.name,
                            "cmd": cmd,
                            "args": arg_str,
                        }))
                        return

                stuff.add_timeout_to(message.author.name)

                if cmd_class.deleteCMDMsg():
                    try:
                        await client.delete_message(message)
                    except discord.errors.NotFound:  # The message has been deleted before
                        pass
            else:
                await client.send_message(message.channel, message.author.mention + " Yetkin yok!")
        else:
            await cmd_class.do(client, message, c_args, cfg)
            stuff.add_timeout_to(message.author.name)

            if cmd_class.deleteCMDMsg():
                try:
                    await client.delete_message(message)
                except discord.errors.NotFound:  # The message has been deleted before
                    pass
    else:
        wc = 0
        wl = []
        for word in message.content.lower().split():
            if wc < 5:
                wc += 1
                if word not in wl:
                    wl.append(word)
                    if stuff.respond.get(word):
                        await client.send_message(message.channel, message.author.mention + " " + stuff.respond.get(word))
                        stuff.add_timeout_to(message.author.name)
        wl = None


def start(config):
    global cfg
    cfg = config
    stuff.respond = config["respond"]

    print("Starting...")
    if not discord.opus.is_loaded():
        # the 'opus' library here is opus.dll on windows
        # or libopus.so on linux in the current directory
        # you should replace this with the location the
        # opus library is located in and with the proper filename.
        # note that on windows this DLL is automatically provided for you
        discord.opus.load_opus('opus')

    client.run(config["token"])
    return 0
