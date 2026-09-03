import functools
import time
import collections

class HotPathCache:
    def __init__(self, capacity=1024):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            
            result = func(*args, **kwargs)
            self.cache[key] = result
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
            return result
        return wrapper

class VectorMath:
    """High-frequency coordinate calculations for gaming frames."""
    @staticmethod
    @HotPathCache(capacity=2048)
    def fast_normalize(x, y, z):
        mag = (x**2 + y**2 + z**2)**0.5
        if mag == 0:
            return 0.0, 0.0, 0.0
        return x / mag, y / mag, z / mag

    @staticmethod
    def batch_process(entities, func):
        return [func(e.x, e.y, e.z) for e in entities]

def throttle(rate_hz):
    interval = 1.0 / rate_hz
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.monotonic()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator