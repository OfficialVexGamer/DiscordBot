import yaml

local_strs = {}


def load_lang(lang: str):
    global local_strs

    with open("lang/{}.yml".format(lang.lower()), "r", encoding="utf8") as f:
        local_strs = yaml.load(f.read())


def get_localized_str(str_id: str, fmt={}):
    if not local_strs[str_id]:
        return "STRING NOT FOUND: {}".format(str_id)

    return str(local_strs[str_id]).format(**fmt)
