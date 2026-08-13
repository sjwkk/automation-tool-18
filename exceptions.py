class GameError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlayerNotFoundError(GameError):
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')

class LevelLoadError(GameError):
    def __init__(self, level_id):
        super().__init__(f'Failed to load level with ID {level_id}.')

class ActionNotAllowedError(GameError):
    def __init__(self, action):
        super().__init__(f'Action {action} is not allowed.')

class ValidationError(GameError):
    def __init__(self, errors):
        super().__init__('Validation errors occurred.')
        self.errors = errors

    def __str__(self):
        return f'{super().__str__()}: {self.errors}'