from bot.commands.command import Command
from bot.commands.none import NoneCommand

muted_chans = {}
server = None
msgChan = "225218131537297408"
commands = Command.__subclasses__()

respond = {
    "sa": "as",
    "op": "hayır."
}


def find_cmd_class(cmd):
    cmd_c = NoneCommand()
    for command in commands:
        cmd_c = command()
        if cmd_c.command is not None:
            if cmd_c().command() == cmd:
                return cmd_c

    return cmd_c
