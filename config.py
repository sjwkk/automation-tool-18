import json
import os

def load_config(file_path, default_config):
    if not os.path.exists(file_path):
        return default_config
    with open(file_path, 'r') as file:
        try:
            user_config = json.load(file)
        except json.JSONDecodeError:
            return default_config
    return {**default_config, **user_config}


def get_configuration():
    default_config = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 75,
        'controls': {
            'jump': 'space',
            'move_left': 'a',
            'move_right': 'd'
        }
    }
    config_path = 'config.json'
    return load_config(config_path, default_config)

if __name__ == '__main__':
    config = get_configuration()
    print(config)