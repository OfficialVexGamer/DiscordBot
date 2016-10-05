from bot import i18n
from bot import stuff
from bot import config
import discord
import os
import sys


class DiscordBot(discord.Client):
    cfg = {}

    def __init__(self, config: list):
        print("Starting...")
        super().__init__()

        self.cfg = config

        if not discord.opus.is_loaded():
            # the 'opus' library here is opus.dll on windows
            # or libopus.so on linux in the current directory
            # you should replace this with the location the
            # opus library is located in and with the proper filename.
            # note that on windows this DLL is automatically provided for you
            discord.opus.load_opus('opus')

        self.run(config["token"])

    async def on_ready(self):
        if not os.path.exists(".avatar_uploaded"):
            with open(self.cfg["avatar"], 'rb') as f:
                print("Uploading avatar...")
                await self.edit_profile(avatar=f.read())
                with open(".avatar_uploaded", 'w') as f2:
                    f2.write(".")
        else:
            print("Avatar already uploaded (wanna change? remove .avatar_uploaded)")

        for chan in self.get_all_channels():
            stuff.muted_chans[chan.name] = False

        for server in self.servers:
            await self.on_server_join(server)

        await self.change_status(game=discord.Game(name=self.cfg["game"]))

        print("Ready! " + self.user.name + " " + self.user.id)

    async def on_server_join(self, server: discord.Server):
        print("Loading config for server: {0} ({1})".format(server.id, server.name))
        config.load_server_config(server.id)
        i18n.load_lang(server.id, config.get_key(server.id, "language"))

    async def on_channel_delete(self, channel: discord.Channel):
        stuff.muted_chans[channel.name] = None

    async def on_channel_create(self, channel: discord.Channel):
        stuff.muted_chans[channel.name] = False

    async def on_error(self, event, *args, **kwargs):
        import traceback
        for server in self.servers:
            for member in server.members:
                if member.name == self.cfg["speak_person"]["name"] and str(member.discriminator) == str(
                        self.cfg["speak_person"]["iden"]):
                    await self.send_message(member, """```python
    
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

    async def on_message(self, message: discord.Message):
        isAuthorAdmin = False
        if type(message.author) == discord.User:  # PM
            if message.author.name == self.cfg["speak_person"]["name"] and str(message.author.discriminator) == str(
                    self.cfg["speak_person"]["iden"]):
                if message.content.startswith('!id '):
                    stuff.msgChan = str(message.content[4:])
                elif message.content.startswith("!name "):
                    await self.edit_profile(username=str(message.content[6:]))
                else:
                    await self.send_message(self.get_channel(stuff.msgChan), message.content)

            return

        for role in message.author.roles:
            for check_role in config.get_key(message.server.id, "admin_roles"):
                if role.name == check_role:
                    isAuthorAdmin = True

        if stuff.muted_chans[message.channel.name]:
            if not isAuthorAdmin:
                await self.delete_message(message)
                await self.send_message(message.author, i18n.get_localized_str(message.server.id, "channel_locked", {"channel":
                                                                                                      message.channel.name}))
                return

        if message.content.startswith('!'):
            if message.author == self.user:
                return

            cmd = message.content[1:].split()[0]
            c_args = message.content[1:].split()[1:]
            cmd_class = stuff.find_cmd_class(cmd)

            print("Komut: (" + message.author.name + ") " + cmd + " args: " + str(c_args))

            if cmd_class.requiresAdmin():
                if isAuthorAdmin:
                    await cmd_class.do(self, message, c_args, self.cfg)
                    for chan in message.server.channels:
                        if chan.name == config.get_key(message.server.id, "modlog_chan"):

                            await self.send_message(chan, "{0} (#{1}): {2}".format(message.author.name,
                                                                                   message.channel.name,
                                                                                   message.content))
                            return

                    if cmd_class.deleteCMDMsg():
                        try:
                            await self.delete_message(message)
                        except discord.errors.NotFound:  # The message has been deleted before
                            pass
                else:
                    await self.send_message(message.channel, i18n.get_localized_str(message.server.id, "bot_noperm", {"mention":
                                                                                                       message.author.name}))
            else:
                await cmd_class.do(self, message, c_args, self.cfg)

                if cmd_class.deleteCMDMsg():
                    try:
                        await self.delete_message(message)
                    except discord.errors.NotFound:  # The message has been deleted before
                        pass