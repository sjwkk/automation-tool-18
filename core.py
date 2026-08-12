from typing import List, Dict, Any

class Game:
    """
    Represents a game instance with various configurations and attributes.
    """
    def __init__(self, title: str, genre: str, settings: Dict[str, Any]) -> None:
        self.title = title
        self.genre = genre
        self.settings = settings

    def start(self) -> None:
        """
        Starts the game and initializes settings.
        """
        print(f"Starting {self.title}...")
        # Initialize settings, graphics, etc.
        for key, value in self.settings.items():
            print(f"Setting {key} to {value}")

    def save(self) -> None:
        """
        Saves the current state of the game.
        """
        print(f"Saving {self.title}...")

    def load(self) -> None:
        """
        Loads the previous game state.
        """
        print(f"Loading {self.title}...")


def create_game(title: str, genre: str, settings: Dict[str, Any]) -> Game:
    """
    Factory function to create a new game instance.
    """
    return Game(title, genre, settings)


games: List[Game] = []


def add_game(game: Game) -> None:
    """
    Adds the game to the game list.
    """
    games.append(game)


def get_game_titles() -> List[str]:
    """
    Retrieves the titles of all games in the list.
    """
    return [game.title for game in games]
