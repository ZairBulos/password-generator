import os
import string
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

FILE = Path(os.getenv('FILE_NAME'))
LENGTH = int(os.getenv('LENGTH'))
CHARS = string.punctuation + string.digits + string.ascii_letters