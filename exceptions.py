class GameError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PlayerNotFoundError(GameError):
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class InvalidMoveError(GameError):
    def __init__(self, message):
        super().__init__(message)

class GameNotStartedError(GameError):
    def __init__(self):
        super().__init__('Game has not been started yet.')

class ConnectionError(GameError):
    def __init__(self, message):
        super().__init__(message)

class InvalidInputError(GameError):
    def __init__(self, input_value):
        super().__init__(f'Invalid input: {input_value}')
        self.input_value = input_value

class GameFullError(GameError):
    def __init__(self):
        super().__init__('Game room is full.')