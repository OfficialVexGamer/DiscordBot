from bot.commands.clear import ClearCommand
from bot.commands.cleverbot import CleverbotCommand
from bot.commands.command import Command
from bot.commands.draw import DrawCommand
from bot.commands.imagemacros import ImageMacroCommand
from bot.commands.lock import LockCommand, UnlockCommand
from bot.commands.mute import MuteCommand
from bot.commands.unmute import UnmuteCommand

muted_chans = {}
server = None
msgChan = "225218131537297408"
commands = {
    "unmute": UnmuteCommand(),
    "mute": MuteCommand(),
    "çekiliş": DrawCommand(),
    "cleverbot": CleverbotCommand(),
    "i": ImageMacroCommand(),
    "help": Command(),
    "kilitle": LockCommand(),
    "kilitac": UnlockCommand(),
    "clear": ClearCommand(),
}