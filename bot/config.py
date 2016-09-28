import os
import yaml

server_config = {}


def create_server_config(id: str):
    with open("conf/cfg-{}.yml".format(id), "w") as f:
        with open("conf/_template.yml") as t:
            f.write(t.read())


def load_server_config(id: str):
    if not os.path.exists(os.path.join("conf/cfg-{}.yml".format(id))):
        create_server_config(id)

    with open("conf/cfg-{}.yml".format(id), "r") as f:
        server_config[id] = yaml.load(f.read())