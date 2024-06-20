import logging
import sys
import os

class Logger:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(current_directory, "logging.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)5s - %(message)s",
        encoding="UTF-8",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    @classmethod
    def info(cls, message):
        logging.info(message)

    @classmethod
    def error(cls, message):
        logging.error(message)

# Example usage
Logger.info("This is an info message")
Logger.error("This is an error message")
