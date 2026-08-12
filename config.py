import json
import os

DEFAULT_CONFIG = {
    'screen_resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'controls': {
        'jump': 'space',
        'shoot': 'ctrl'
    }
}

def load_config(file_path='config.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            user_config = json.load(f)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config()
    print(config)