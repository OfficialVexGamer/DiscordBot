from queue import Queue
from bot.commands import NoneCommand, Command
import inspect
import bot.commands

muted_chans = {}
server = None
msgChan = "225218131537297408"
# noinspection PyUnresolvedReferences
commands = inspect.getmembers(bot.commands, predicate=lambda o: inspect.isclass(o) and issubclass(o, Command))
timeout = {}
bot_version = "1.3.0"


def find_cmd_class(cmd: str):
    cmd_c = NoneCommand()
    for command in commands:
        cmd_c = (command[1])()
        if cmd_c.command() != "_____________nonecommandsrsly":
            if cmd_c.command() == cmd:
                return cmd_c

    return NoneCommand()