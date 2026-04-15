# ============================================================
# @license (c) Alexander Soviet9773Red - https://github.com/Soviet9773Red/
# main.py (CLI launcher)
# ============================================================
"""
wine-data/
├─ data/
│ ├── wine-data-raw.csv
│ ├──  ...
│ └──  ...
├─ outputs/
│ └── bias_report_YYYY-MM-DD_hhmmss.txt
├── tools/
│ ├── init.py
│ └── logger.py
├─ main.py
├── scripts/
└── hearts-*.py

Data types:
data/
├── wine-data-raw.csv       # raw data
├── wine-clean.csv          # after data-clean.py
├── wine-prepared-3.csv     # three quality classes: low / medium / high
└── wine-prepared-2.csv     # binary quality classes: ordinary / high
"""
import sys
import subprocess

# Run script helper
# -------------------------
def run_script(script_name):
    print(f"\n> Running {script_name}...\n")
    subprocess.run([sys.executable, script_name])
    print("\n> Done.")

# Menu
# -------------------------
def show_menu():
    print(
        "\n🍷 Wine Quality Classifier · SETUP\n"
        " === DATA ===\n"
        "0. View raw data - wine-data-raw.csv\n"
        "1. Clean .csv data\n"
        "2. Visualize cleaned data\n"
        "3. Prepare data for models\n\n"

        " === Models and tuning. === \n"

        "4.  Decision Tree\n"
        "5.  k-NN model\n"
        "6.  Random Forest\n"

        "\n === APPLICATION ===\n"
        "Wine QC:\nRun  python scripts\wine-test.py after exit \n\n"

        " === SYSTEM ===\n"
        "m Menu | x exit\n"
    )

# Main loop
# -------------------------
def main():
    show_menu()

    while True:
        choice = input("Menu(m) · Wine QS> Select option: ")

        if choice == "m":
            show_menu()

        elif choice == "0":
            run_script("scripts/data-preview.py")

        elif choice == "1":
            run_script("scripts/data-clean.py")

        elif choice == "2":
            run_script("scripts/data-vis.py")

        elif choice == "3":
            run_script("scripts/data-prepare.py")

        elif choice == "4":
            run_script("scripts/dtree.py")

        elif choice == "5":
            run_script("scripts/knn.py")

        elif choice == "6":
            run_script("scripts/rf.py")  


        elif choice == "x":
            print("> Exiting...")
            break

        else:
            print("> Invalid input")

        print()

# Start
# -------------------------
main() if __name__ == "__main__" else None