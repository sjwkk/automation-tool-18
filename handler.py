import json
from typing import List, Dict, Any


def load_game_data(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_games_by_genre(game_data: List[Dict[str, Any]], genre: str) -> List[Dict[str, Any]]:
    return [game for game in game_data if game.get('genre') == genre]


def calculate_average_score(game_data: List[Dict[str, Any]]) -> float:
    total_score = sum(game.get('score', 0) for game in game_data)
    return total_score / len(game_data) if game_data else 0.0


def update_game_score(game_data: List[Dict[str, Any]], game_id: str, new_score: float) -> None:
    for game in game_data:
        if game['id'] == game_id:
            game['score'] = new_score
            break

