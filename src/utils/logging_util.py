import logging
import os
from datetime import datetime

# Define the directory to store log files
log_directory = os.path.join(os.path.dirname(__file__), '..', 'execution_results', 'logs')

# Create the log directory if it does not exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate a timestamp for the log file name
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_path = os.path.join(log_directory, f'{timestamp}.log')

# Configure logging settings
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
