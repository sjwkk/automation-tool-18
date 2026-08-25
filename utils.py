from typing import List, Dict, Tuple, Optional, Any, Callable
import math
import random
import time

def calculate_farming_efficiency(resources: Dict[str, int], time_spent: float) -> float:
    """Calculate the efficiency of resource farming in the game.
    Uses logarithmic scaling as an unusual approach to reward higher volumes
    disproportionately for automation balancing.
    """
    total_resources = sum(resources.values())
    if total_resources == 0 or time_spent <= 0:
        return 0.0
    base_efficiency = total_resources / time_spent
    scaled = base_efficiency * math.log(total_resources + 1)
    return round(scaled, 2)

def find_nearest_resource(
    current_pos: Tuple[int, int], resources: List[Tuple[int, int, str]]
) -> Optional[Tuple[int, int, str]]:
    """Locate the nearest game resource from current position.
    Creative tie-breaking uses hash of resource name to select among equals.
    Returns None if no resources available.
    """
    if not resources:
        return None
    min_distance = float("inf")
    nearest: Optional[Tuple[int, int, str]] = None
    for x, y, name in resources:
        distance = math.sqrt((x - current_pos[0]) ** 2 + (y - current_pos[1]) ** 2)
        if distance < min_distance or (
            distance == min_distance
            and (hash(name) < hash(nearest[2]) if nearest else True)
        ):
            min_distance = distance
            nearest = (x, y, name)
    return nearest

def simulate_automation_cycle(
    actions: List[Callable[[], None]], max_cycles: int = 10
) -> int:
    """Simulate a series of automation actions over multiple cycles.
    Unusual approach incorporates 10 percent random skips to mimic human variance.
    Returns the count of completed cycles.
    """
    successful_cycles = 0
    for _ in range(max_cycles):
        for action in actions:
            if random.random() > 0.1:
                action()
        successful_cycles += 1
        time.sleep(0.001)  # short simulated delay
    return successful_cycles

def parse_game_log(line: str) -> Dict[str, Any]:
    """Parse a single line from the game log into a dictionary.
    Attempts to convert values to int or float where possible.
    """
    if ":" not in line:
        return {"raw": line.strip()}
    key, value = line.split(":", 1)
    key = key.strip().lower()
    value = value.strip()
    try:
        parsed_value: Any = int(value)
    except ValueError:
        try:
            parsed_value = float(value)
    except ValueError:
        parsed_value = value
    return {key: parsed_value}

def generate_session_seed(player_name: str, level: int) -> int:
    """Generate a deterministic seed for game session randomness.
    Employs unusual bitwise operations for creative uniqueness.
    """
    base = hash(player_name) + level * 1000
    seed = (base << 4) ^ (base >> 2)  # bit shift and xor
    seed = seed & 0xFFFFFFFF  # mask to 32 bits
    return abs(seed) % 999999 + 1