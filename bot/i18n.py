import yaml

server_langs = {}


def load_lang(server: int, lang: str):
    global server_langs

    with open("lang/{}.yml".format(lang.lower()), "r", encoding="utf8") as f:
        server_langs[server] = yaml.load(f.read())


def get_localized_str(server: int, str_id: str, fmt={}):
    if server_langs[server].get(str_id):
        return str(server_langs[server][str_id]).format(**fmt)

    return "STRING NOT FOUND: {}".format(str_id)
