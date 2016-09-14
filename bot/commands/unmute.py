from bot.commands.command import Command


class UnmuteCommand(Command):
    def requiresAdmin(self):
        return True

    async def do(self, client, message, args, config={}):
        if not config["mute_role"]:
            await client.send_message(message.channel, message.author.mention +
                                      ": Bot Konfigurasyon hatası! (mute_role bulunamadı)")
            return

        if not config["admin_roles"]:
            await client.send_message(message.channel, message.author.mention +
                                      ": Bot Konfigurasyon hatası! (admin_roles bulunamadı)")
            return

        for member in message.channel.server.members:
            if args[0].lower() == member.name.lower():
                for role in member.roles:
                    for check_role in config["admin_roles"]:
                        if role.name == check_role:
                            await client.send_message(message.channel, message.author.mention +
                                                      " Bir admini muteleyemessin!")
                            return
                        elif role.name == config["mute_role"]:
                            await client.remove_roles(member, role)
                            await client.send_message(message.channel, "@" + member.name + " Artık konuşabilir")
                            return

        await client.send_message(message.channel, message.author.mention + " Böyle bir kişi yok!")
