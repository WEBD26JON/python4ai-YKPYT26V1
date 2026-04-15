# Raw data viewer (Pandas)
from pathlib import Path
import sys
import io
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.logger import log, make_log_filename

import pandas as pd

# 1. Load data
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
fn = make_log_filename("data-preview")

df = pd.read_csv(DATA_DIR / "wine-data-raw.csv")

log("\n=== RAW DATA (HEAD) ===", fn)
log(df.head(), fn)

log("\n=== RAW INFO ===", fn)
#log(df.info(), fn) # Not work, df.info() do not returns string, and prints direct , None as a result
buffer = io.StringIO() # To bufferize output
df.info(buf=buffer)
log(buffer.getvalue(), fn)

log("\n=== RAW DESCRIBE ===", fn)
log(df.describe(), fn)