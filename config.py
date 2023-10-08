import os
import string
from dotenv import load_dotenv

load_dotenv()

LENGTH = int(os.getenv('LENGTH'))
CHARS = string.punctuation + string.digits + string.ascii_letters