import random
from config import CHARS, LENGTH

def generate_password():
    return ''.join(random.sample(CHARS, LENGTH))