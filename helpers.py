import json
from typing import Dict, List, Any, Union
from collections import defaultdict
import math

def parse_raw_gaming_data(raw_input: str) -> Dict[str, Any]:
    try:
        data = json.loads(raw_input)
        if not isinstance(data, dict):
            data = {"events": data} if isinstance(data, list) else {"value": data}
        return data
    except json.JSONDecodeError:
        return {"error": "invalid json", "raw": raw_input[:100]}

def normalize_gaming_scores(scores: Dict[str, Union[int, float]]) -> Dict[str, float]:
    normalized = {}
    if not scores:
        return normalized
    max_val = max(scores.values()) if scores else 1
    for player, score in scores.items():
        if score > 0:
            log_score = math.log(score + 1)
            normalized[player] = (log_score / (math.log(max_val + 1) + 1))
        else:
            normalized[player] = 0.0
    return normalized

def aggregate_game_sessions(sessions: List[Dict[str, Any]]) -> Dict[str, Any]:
    summary = {
        "total_players": 0,
        "total_score": 0,
        "player_stats": defaultdict(lambda: {"score": 0, "matches": 0, "avg": 0})
    }
    all_players = set()
    for session in sessions:
        if not isinstance(session, dict):
            continue
        players = session.get("players", {})
        for player, pdata in players.items():
            if isinstance(pdata, dict):
                score = pdata.get("score", 0)
                summary["player_stats"][player]["score"] += score
                summary["player_stats"][player]["matches"] += 1
                all_players.add(player)
            elif isinstance(pdata, (int, float)):
                summary["player_stats"][player]["score"] += pdata
                summary["player_stats"][player]["matches"] += 1
                all_players.add(player)
        summary["total_score"] += session.get("total_score", 0)
    summary["total_players"] = len(all_players)
    for player, stats in summary["player_stats"].items():
        if stats["matches"] > 0:
            stats["avg"] = stats["score"] / stats["matches"]
    summary["player_stats"] = dict(summary["player_stats"])
    return summary

def filter_valid_gaming_events(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    required = {"type", "timestamp", "player"}
    valid_events = []
    for event in events:
        if isinstance(event, dict) and required.issubset(set(event.keys())):
            if event.get("timestamp", 0) > 0 and event.get("player"):
                valid_events.append(event)
    return valid_events

def generate_leaderboard(aggregated: Dict[str, Any]) -> List[Dict[str, Any]]:
    player_stats = aggregated.get("player_stats", {})
    leaderboard = []
    for player, stats in player_stats.items():
        entry = {
            "player": player,
            "total_score": stats["score"],
            "matches_played": stats["matches"],
            "average_score": round(stats.get("avg", 0), 2)
        }
        leaderboard.append(entry)
    leaderboard.sort(key=lambda x: x["total_score"], reverse=True)
    for i, entry in enumerate(leaderboard, 1):
        entry["rank"] = i
    return leaderboard