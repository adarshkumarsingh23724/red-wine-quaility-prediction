import os
import sys
import logging

# Log format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory and file path for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  # ✅ fixed typo

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)   # ✅ added comma
    ]
)

# Create logger instance
logger = logging.getLogger("redwinequalitypredictionLogger")