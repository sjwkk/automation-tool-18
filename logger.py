import logging
import os
from logging.handlers import RotatingFileHandler

def get_gaming_logger(name='automation-tool-18'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    log_path = 'logs/game_engine.log'
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_path, maxBytes=1024 * 1024 * 5, backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

log = get_gaming_logger()