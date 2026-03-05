
from dotenv import load_dotenv

import os

def load_config():
    load_dotenv()

    config = {
        "mode": os.getenv("MATRIX_MODE", "development")

    }
    