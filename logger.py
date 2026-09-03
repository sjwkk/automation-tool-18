import sys
import logging
import traceback
from collections import deque
from typing import Any, Callable

class QuantumGamingLogger(logging.Logger):
    """Resilient logger that catches unprintable game chat, corrupt memory
    payloads, and write race conditions without interrupting bot loops."""

    def __init__(self, name: str, level: int = logging.INFO, capacity: int = 50):
        super().__init__(name, level)
        self._fallback_ring: deque = deque(maxlen=capacity)

    def makeRecord(self, *args: Any, **kwargs: Any) -> logging.LogRecord:
        try:
            return super().makeRecord(*args, **kwargs)
        except Exception as exc:
            return logging.LogRecord(
                self.name, logging.ERROR, __file__, 0,
                f"[LOG_CORRUPTION_RECOVERED] Exception: {exc}", (), None
            )

    def handle(self, record: logging.LogRecord) -> None:
        try:
            if isinstance(record.msg, bytes):
                record.msg = record.msg.decode("utf-8", errors="backslashreplace")
            elif not isinstance(record.msg, str):
                record.msg = repr(record.msg)
            super().handle(record)
        except Exception as err:
            self._fallback_ring.append({
                "msg": getattr(record, "msg", "UNREADABLE"),
                "err": str(err),
                "trace": traceback.format_exc()
            })
            sys.stderr.write(f"![LOG_FAILOVER] Stash size: {len(self._fallback_ring)}\n")

    def recover_emergency_logs(self) -> list[dict[str, Any]]:
        recovered = list(self._fallback_ring)
        self._fallback_ring.clear()
        return recovered

def safe_log_execution(logger_instance: QuantumGamingLogger) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger_instance.error(f"Panic trapped in {func.__name__}: {e}")
                return None
        return wrapper
    return decorator
