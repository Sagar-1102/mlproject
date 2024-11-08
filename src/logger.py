import logging
import os
from datetime import datetime

# Generate a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for the logs directory
logs_path = os.path.join(os.getcwd(), "logs")

# Ensure the directory exists
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Print paths for debugging purposes
print(f"Current Working Directory: {os.getcwd()}")
print(f"Logs Path: {logs_path}")
print(f"Log File Path: {LOG_FILE_PATH}")

# Additional check to ensure the directory and file can be accessed
try:
    with open(LOG_FILE_PATH, 'w') as f:
        f.write("Test write to log file.\n")
    print("Log file created and written to successfully.")
except Exception as e:
    print(f"Failed to create or write to log file: {e}")

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Example usage
if __name__ == "__main__":
    logging.info("This is an info log.")
    logging.warning("This is a warning log.")
    logging.error("This is an error log.")
    print("Logging setup complete, log messages should now be recorded.")
