import logging
import os
from datetime import datetime

# Generate log file name based on the current timestamp.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Get the directory where the logger.py file is located.
root_dir = os.path.dirname(os.path.abspath(__file__))

# Set logs_path to a writable location, either relative to your app or to a standard temp directory.
# Using a directory within your project:
logs_path = os.path.join(root_dir, "..", "logs")

# Or, you can use a temporary directory:
# logs_path = "/tmp/logs"

# Ensure the logs directory exists.
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file.
log_file_path = os.path.join(logs_path, LOG_FILE)

# Set the logging configuration.
logging.basicConfig(
    filename=log_file_path,
    format=" [%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example usage
# logging.info("Logging has started")
