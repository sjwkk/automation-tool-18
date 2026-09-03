import os
import json
from typing import Any, Dict

class GameConfig:
    """Dynamic configuration loader with auto-merging defaults for gaming automation."""
    DEFAULTS: Dict[str, Any] = {
        "target_fps": 60,
        "click_delay_ms": 150,
        "hotkey_start": "F10",
        "hotkey_stop": "F11",
        "confidence_threshold": 0.85,
        "pixel_matching_tolerance": 10,
        "debug_overlay": False
    }

    def __init__(self, filepath: str = "config.json"):
        self._filepath = filepath
        self._loaded_config: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        if os.path.exists(self._filepath):
            try:
                with open(self._filepath, "r", encoding="utf-8") as f:
                    self._loaded_config = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._loaded_config = {}
        else:
            self._loaded_config = {}

    def __getattr__(self, name: str) -> Any:
        env_key = f"GAME_{name.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            if name in self.DEFAULTS:
                try:
                    if isinstance(self.DEFAULTS[name], bool):
                        return val.lower() in ("true", "1", "yes")
                    return type(self.DEFAULTS[name])(val)
                except ValueError:
                    pass
            return val

        if name in self._loaded_config:
            return self._loaded_config[name]

        if name in self.DEFAULTS:
            return self.DEFAULTS[name]

        raise AttributeError(f"Configuration setting '{name}' is not defined.")

    def save(self) -> None:
        current_data = {k: getattr(self, k) for k in self.DEFAULTS}
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(current_data, f, indent=4)
