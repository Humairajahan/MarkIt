import os
import logging
from dotenv import load_dotenv

load_dotenv("backend_server/.env")


class Logger:
    def __init__(self):
        self.fileName = os.getenv("LOGGER_FILE_NAME")

    def log(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        file_handler = logging.FileHandler(self.fileName)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger


logger = Logger().log()
