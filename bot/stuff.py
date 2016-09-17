from bot.commands import NoneCommand
from collections import defaultdict
import inspect
import bot.commands

muted_chans = defaultdict(dict)
server = None
msgChan = "225218131537297408"
# noinspection PyUnresolvedReferences
commands = inspect.getmembers(bot.commands,
                              predicate=lambda o: inspect.isclass(o) and issubclass(o, bot.commands.Command))
respond = defaultdict(dict)
timeout = defaultdict(dict)


def find_cmd_class(cmd):
    cmd_c = NoneCommand()
    for command in commands:
        cmd_c = (command[1])()
        if cmd_c.command() != "_____________nonecommandsrsly":
            if cmd_c.command() == cmd:
                return cmd_c

    return NoneCommand()
