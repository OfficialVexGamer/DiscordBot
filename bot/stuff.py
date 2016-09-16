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
    for command in commands:
        if command.command is not None:
            if command.command() == cmd:
                return command

    return NoneCommand()
