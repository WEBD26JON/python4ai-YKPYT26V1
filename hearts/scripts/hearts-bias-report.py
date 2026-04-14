import sys
from pathlib import Path
from datetime import datetime
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.logger import log, make_log_filename

import pandas as pd

# Load prepared data
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

df = pd.read_csv(DATA_DIR / "heart_prepared.csv")
file_name = make_log_filename("bias_report")

log("=== BIAS / DATA DISTRIBUTION REPORT ===\n", file_name)

# 1. Target balance
# -------------------------
log("--- Target distribution (AHD) ---", file_name)
log(df["ahd"].value_counts(normalize=True), file_name)

# 2. Sex vs disease
# -------------------------
log("\n--- Sex vs AHD ---", file_name)
log(pd.crosstab(df["sex"], df["ahd"], normalize="index"), file_name)

# 3. Age vs disease
# -------------------------
log("\n--- Age stats by AHD ---", file_name)
log(df.groupby("ahd")["age"].describe(), file_name)

# 4. Chest pain vs disease
# -------------------------
cp_cols = [col for col in df.columns if "chest_pain" in col]

log("\n--- Chest pain vs AHD ---", file_name)
for col in cp_cols:
    log(f"\n{col}:", file_name)
    log(pd.crosstab(df[col], df["ahd"], normalize="index"), file_name)

# 5. Mean values by class
# -------------------------
log("\n--- Mean feature values by AHD ---", file_name)
log(df.groupby("ahd").mean(numeric_only=True), file_name)

# 6. Save report
# -------------------------
output_file = BASE_DIR / "outputs" / file_name
log (f"End of report: {file_name}",  file_name)
print(f"\nReport saved to: {output_file}")

# with open(output_file, "w") as f:
#     f.write("BIAS REPORT\n")
#     f.write("\nTarget distribution:\n")
#     f.write(str(df["ahd"].value_counts(normalize=True)))

