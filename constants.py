class ImmutableConstantError(TypeError):
    pass

class ConstantMeta(type):
    def __setattr__(cls, name, value):
        raise ImmutableConstantError(f"cannot rebind constant '{name}'")
    
    def __delattr__(cls, name):
        raise ImmutableConstantError(f"cannot delete constant '{name}'")

class GameConstants(metaclass=ConstantMeta):
    # Keyboard virtual keys for game control injection
    KEY_ATTACK = 0x58      # 'X' key
    KEY_JUMP = 0x43        # 'C' key
    KEY_DASH = 0x10        # Shift key
    KEY_INVENTORY = 0x49   # 'I' key

    # Detection colors (Hex representation)
    COLOR_HEALTH_LOW = 0xFF0033
    COLOR_MANA_FULL = 0x0066FF
    COLOR_NPC_NAME = 0x00FF66

    # Engine delays and tick rates (seconds)
    TICK_RATE_UI = 0.25
    TICK_RATE_COMBAT = 0.05
    COOLDOWN_DASH_MS = 800

    @classmethod
    def to_rgb(cls, hex_color: int) -> tuple:
        """Converts hex integer color representation to RGB tuple."""
        r = (hex_color >> 16) & 0xFF
        g = (hex_color >> 8) & 0xFF
        b = hex_color & 0xFF
        return (r, g, b)

    @classmethod
    def get_combat_keys(cls) -> list:
        return [cls.KEY_ATTACK, cls.KEY_JUMP, cls.KEY_DASH]