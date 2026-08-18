import json
from typing import Any, Dict, List

class GameData:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    def filter_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        return [game for game in self.data if game.get('genre') == genre]

    def sort_by_rating(self) -> List[Dict[str, Any]]:
        return sorted(self.data, key=lambda x: x.get('rating', 0), reverse=True)

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'name': 'Game A', 'genre': 'Adventure', 'rating': 4.5},
        {'name': 'Game B', 'genre': 'RPG', 'rating': 4.9},
        {'name': 'Game C', 'genre': 'RPG', 'rating': 4.3},
        {'name': 'Game D', 'genre': 'Adventure', 'rating': 4.7},
    ]
    game_data = GameData(sample_data)
    rpg_games = game_data.filter_by_genre('RPG')
    sorted_games = game_data.sort_by_rating()
    print(game_data.to_json())
    print(rpg_games)
    print(sorted_games)