import os
import yaml

server_config = {}
template_conf = {}


def create_server_config(id: str):
    with open("conf/cfg-{}.yml".format(id), "w") as f:
        yaml.dump(template_conf, f, default_flow_style=False,
                  allow_unicode=True)


def load_template_config():
    global template_conf

    with open("conf/_template.yml", "r") as f:
        template_conf = yaml.load(f.read())


def load_server_config(id: str):
    if not os.path.exists(os.path.join("conf/cfg-{}.yml".format(id))):
        create_server_config(id)

    with open("conf/cfg-{}.yml".format(id), "r") as f:
        server_config[id] = yaml.load(f.read())


def save_server_config(id):
    with open("conf/cfg-{}.yml".format(id), "w") as f:
        yaml.dump(server_config[id], f, default_flow_style=False, allow_unicode=True)


def check_config(id: str, key: str):
    if server_config[id].get(key):
        return server_config[id][key]

    if template_conf.get(key):
        server_config[id] = template_conf
        save_server_config(id)
        return template_conf[key]

    return "KEY NOT FOUND"


def get_key(id: str, key: str):
    if not server_config[id]:
        create_server_config(id)

    return check_config(id, key)


def set_key(id: str, key: str, val: object):
    if not server_config[id]:
        create_server_config(id)

    if check_config(id, key) != "KEY NOT FOUND":
        server_config[id][key] = val
        save_server_config(id)
