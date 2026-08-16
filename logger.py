import logging
import os

class Logger:
    def __init__(self, name, log_file='app.log', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)
        self._check_file_size(log_file)

    def _check_file_size(self, log_file):
        if os.path.exists(log_file) and os.path.getsize(log_file) > 10485760:  # 10 MB limit
            self.logger.warning('Log file size exceeded. Archiving...')
            self._archive_log(log_file)

    def _archive_log(self, log_file):
        try:
            os.rename(log_file, log_file.replace('.log', '_backup.log'))
            self.logger.info('Log archived successfully.')
        except Exception as e:
            self.logger.error(f'Error archiving log: {e}')

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

# Usage example
if __name__ == '__main__':
    logger = Logger(__name__)
    logger.log_info('Logger initialized. Happy gaming!')