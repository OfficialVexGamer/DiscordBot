from bot.Bot import DiscordBot
import yaml


def get_config():
    with open("config.yml", "r", encoding="utf8") as f:
        return yaml.load(f.read())


def main():
    DiscordBot(get_config())
    return 0

if __name__ == "__main__":
    exit(main())