from discord import Role

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

        for member in message.channel.server.members:
            if args[0].lower() == member.name.lower():
                for role in member.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            print(role.name)
                            await client.send_message(message.channel, "@" + message.author.name +
                                                      " Bir admini muteleyemessin!")
                            return

                for role in list(client.servers)[0].roles:
                    print(role.name)
                    if role.name == config["mute_role"]:
                        client.add_roles(member, role)
                        await client.send_message(message.channel, "@" + member.name + " Mutelendi")
                        return

                await client.send_message(message.channel, "@" + message.author.name + " Mute rolü yok!")
                return

        await client.send_message(message.channel, "@" + message.author.name + " Böyle bir kişi yok!")
