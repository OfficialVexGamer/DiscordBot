from bot.commands.command import Command


class MuteCommand(Command):
    def requiresAdmin(self):
        return True

    async def do(self, client, message, args, config={}):
        if not config["mute_role"]:
            await client.send_message(message.channel, "@" + message.author.name +
                                      ": Bot Konfigurasyon hatası! (mute_role bulunamadı)")
            return

        if not config["admin_roles"]:
            await client.send_message(message.channel, "@" + message.author.name +
                                      ": Bot Konfigurasyon hatası! (admin_roles bulunamadı)")
            return

        nameToMute = ""
        for arg in args[1:]:
            nameToMute = nameToMute + " " + nameToMute

        for member in message.channel.server.members:
            if nameToMute.lower() == member.name.lower():
                for role in member.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            print(role.name)
                            await client.send_message(message.channel, "@" + message.author.name +
                                                      " Bir admini muteleyemessin!")
                            return

                for role in list(client.servers)[0].roles:
                    if role.name == config["mute_role"]:
                        await client.add_roles(member, role)

                        reason = ""
                        for arg in args[1:]:
                            reason = reason + " " + arg

                        await client.send_message(message.channel, "@" + member.name + " Susturuldu: " + reason)
                        return

                await client.send_message(message.channel, "@" + message.author.name + " Mute rolü yok!")
                return

        await client.send_message(message.channel, "@" + message.author.name + " Böyle bir kişi yok!")
