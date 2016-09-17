import inspect
import bot.commands
from bot.commands import NoneCommand

muted_chans = {}
server = None
msgChan = "225218131537297408"
# noinspection PyUnresolvedReferences
commands = inspect.getmembers(bot.commands,
                              predicate=lambda o: inspect.isclass(o) and issubclass(o, bot.commands.Command))

respond = {
    "sa": "as",
    "op": "hayır."
}


def find_cmd_class(cmd):
    cmd_c = NoneCommand()
    for command in commands:
        cmd_c = (command[1])()
        if cmd_c.command() != "_____________nonecommandsrsly":
            if cmd_c.command() == cmd:
                return cmd_c

    return NoneCommand()
