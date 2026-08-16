import json
import random
from typing import List, Dict, Any

class GameProcessor:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data
        self.processed_data = []

    def process_games(self) -> None:
        self.processed_data = [self._process_single_game(game) for game in self.data]

    def _process_single_game(self, game: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'name': game['name'],
            'player_count': self._simulate_player_count(),
            'rating': self._calculate_rating(game['reviews']),
        }

    def _simulate_player_count(self) -> int:
        return random.randint(1, 1000)

    def _calculate_rating(self, reviews: int) -> float:
        return min(5.0, round(reviews / 20, 1))

    def get_processed_data(self) -> str:
        return json.dumps(self.processed_data, indent=4)

# Example usage
if __name__ == '__main__':
    game_data = [
        {'name': 'Game A', 'reviews': 150},
        {'name': 'Game B', 'reviews': 99},
        {'name': 'Game C', 'reviews': 250},
    ]
    processor = GameProcessor(game_data)
    processor.process_games()
    print(processor.get_processed_data())