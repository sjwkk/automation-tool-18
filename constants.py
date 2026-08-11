GAMING_CONSTANTS = {
    'MAX_PLAYERS': 4,
    'DEFAULT_MAP': 'Forest',
    'VERSION': '1.0.0',
}

class GameConfigError(Exception):
    pass

def get_game_constant(key):
    try:
        value = GAMING_CONSTANTS[key]
    except KeyError:
        raise GameConfigError(f'Constant {key} not found.')
    return value

if __name__ == '__main__':
    try:
        print(get_game_constant('MAX_PLAYERS'))
        print(get_game_constant('INVALID_KEY'))
    except GameConfigError as e:
        print(f'Error: {e}')
