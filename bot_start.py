from bot import Bot
import yaml


def get_config():
    with open("config.yml", "r") as f:
        return yaml.load(f.read())


def main():
    return Bot.start(get_config())

if __name__ == "__main__":
    exit(main())