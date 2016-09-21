from bot.commands.command import Command


class MuteCommand(Command):
    def requiresAdmin(self):
        return True

    def deleteCMDMsg(self):
        return True

    def command(self):
        return "mute"

    async def do(self, client, message, args, config={}):
        if not config["mute_role"]:
            await client.send_message(message.channel, message.author.mention +
                                      ": Bot Konfigurasyon hatası! (mute_role bulunamadı)")
            return

        if not config["admin_roles"]:
            await client.send_message(message.channel, message.author.mention +
                                      ": Bot Konfigurasyon hatası! (admin_roles bulunamadı)")
            return

        nameToMute = ""
        for arg in args:
            nameToMute = nameToMute + " " + arg

        for member in message.channel.server.members:
            if nameToMute.lower().strip() == member.name.lower():
                for role in member.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            await client.send_message(message.channel, message.author.mention +
                                                      " Bir admini muteleyemessin!")
                            return

                for role in message.server.roles:
                    if role.name.lower() == config["mute_role"].lower():
                        await client.add_roles(member, role)
                        await client.send_message(message.channel, member.mention + " Susturuldu")
                        return

                await client.send_message(message.channel, message.author.mention + " Mute rolü yok!")
                return

        await client.send_message(message.channel, message.author.mention + " Böyle bir kişi yok!")
