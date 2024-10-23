import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

root_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path one directory above the current working directory.
logs_path = os.path.join(root_dir,"..", "logs")

# Ensure the logs directory exists.
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file.
log_file_path = os.path.join(logs_path, LOG_FILE)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = " [%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

# if __name__== "__main__":
#     logging.info("logging has started")
