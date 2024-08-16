import logging
from enum import Enum


class Colors(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class ColoredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": (3, Colors.OKBLUE.value),
        "INFO": (4, Colors.OKGREEN.value),
        "WARNING": (1, Colors.WARNING.value),
        "ERROR": (3, Colors.FAIL.value),
        "CRITICAL": (0, Colors.HEADER.value),
    }

    def format(self, record):
        if self.COLORS.get(record.levelname) is None:
            return super().format(record)

        padding, color = self.COLORS.get(record.levelname)
        record.name = record.name.rjust(padding + len(record.name))
        record.levelname = f"{color}{record.levelname}{Colors.ENDC.value}"

        return super().format(record)


class Logger:
    def __init__(self, module_name: str = __name__):
        self.module_name = module_name
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.DEBUG)  # Set to lowest level to catch all messages

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = ColoredFormatter("%(levelname)s: %(name)s - %(message)s")

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# Example usage
if __name__ == "__main__":
    ...
