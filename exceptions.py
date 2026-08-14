class GameError(Exception):
    """Base class for all exceptions related to game operations."""
    pass

class InvalidPlayerError(GameError):
    """Raised when a player is invalid."""
    def __init__(self, player_name):
        super().__init__(f"Invalid player: {player_name}")
        self.player_name = player_name

class GameNotFoundError(GameError):
    """Raised when a requested game cannot be found."""
    def __init__(self, game_id):
        super().__init__(f"Game not found: {game_id}")
        self.game_id = game_id

class ScoreError(GameError):
    """Raised for score related exceptions."""
    def __init__(self, message):
        super().__init__(message)

def handle_score_submission(score):
    if score < 0:
        raise ScoreError("Score cannot be negative")
    # Additional logic for score submission

try:
    handle_score_submission(-1)
except ScoreError as e:
    print(f"Error: {e}")

try:
    raise InvalidPlayerError("JohnDoe")
except InvalidPlayerError as e:
    print(f"Error: {e}")

try:
    raise GameNotFoundError(42)
except GameNotFoundError as e:
    print(f"Error: {e}")