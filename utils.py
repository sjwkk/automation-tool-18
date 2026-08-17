from typing import List, Dict, Any


def calculate_average(scores: List[float]) -> float:
    """Calculate the average of a list of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def filter_high_scores(scores: List[float], threshold: float) -> List[float]:
    """Filter scores greater than the given threshold."""
    return [score for score in scores if score > threshold]


def format_scoreboard(player_scores: Dict[str, float]) -> str:
    """Format a scoreboard string from player scores dictionary."""
    sorted_scores = sorted(player_scores.items(), key=lambda item: item[1], reverse=True)
    formatted_scores = '\n'.join(f'{player}: {score:.2f}' for player, score in sorted_scores)
    return formatted_scores


def get_top_player(player_scores: Dict[str, float]) -> str:
    """Get the name of the player with the highest score."""
    if not player_scores:
        return "No players"
    top_player = max(player_scores, key=player_scores.get)
    return top_player


def save_scores_to_file(scores: Dict[str, float], filename: str) -> None:
    """Save player scores to a file."""
    with open(filename, 'w') as file:
        for player, score in scores.items():
            file.write(f'{player},{score}\n')
