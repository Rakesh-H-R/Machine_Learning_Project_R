import logging
from datetime import date, datetime
import os

LOG_DIR = "housing-logs"
CURRENT_TIME = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f"log_{CURRENT_TIME}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, file_name)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )