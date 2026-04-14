# tools/logger.py

from pathlib import Path
from datetime import datetime

# Time stamp to file name
def make_log_filename(base_name="log"):
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S") 
    return f"{base_name}_{ts}.txt"

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"

def log(message, filename="log.txt", console=True):
    OUTPUT_DIR.mkdir(exist_ok=True)

    if console:
        print(message)

    with open(OUTPUT_DIR / filename, "a", encoding="utf-8") as f:
        f.write(str(message) + "\n")