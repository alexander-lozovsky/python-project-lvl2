import json

import yaml

loaders = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}


def load_file(file_object, extention):
    loader = loaders[extention]
    return loader(file_object)
