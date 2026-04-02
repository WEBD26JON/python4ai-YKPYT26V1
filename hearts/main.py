# ============================================================
# @license (c) Alexander Soviet9773Red - https://github.com/Soviet9773Red/
# 🧠 main.py (CLI launcher)
# ============================================================
# project/
# ├─ .venv
# ├─ data/
# ├─ scripts/
# │   ├─ hearts-*.py
# ├─ outputs/
# ├─ main.py

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
        "\nHEART PROJECT\n"
        " === DATA ===\n"
        "0. View raw data - hearts.csv\n"
        "1. Clean .csv data\n"
        "2. Visualize cleaned data\n"
        "3. Prepare data for models\n\n"

        " === Models tuning. === \n"

        "4.  Logistic Regression (no scaling)\n"
        "5.  Logistic Regression (scaled)\n"
        "6.  k-NN model with different k \n"
        "7.  Decision Tree\n"
        "8.  Random Forest\n\n"

        " === APPLICATION ===\n"
        "9. Patient's diagnostic.\n\n"

        " === SYSTEM ===\n"
        "m Menu\n"
        "e exit\n"
    )

# Main loop
# -------------------------
def main():
    show_menu()

    while True:
        choice = input("HEART PROJECT (m for Menu) > Select option: ")

        if choice == "m":
            show_menu()

        elif choice == "0":
            run_script("scripts/hearts-raw-preview.py")

        elif choice == "1":
            run_script("scripts/hearts-data-clean.py")

        elif choice == "2":
            run_script("scripts/hearts-vis.py")

        elif choice == "3":
            run_script("scripts/hearts-prepare.py")

        elif choice == "4":
            run_script("scripts/hearts-logreg.py")

        elif choice == "5":
            run_script("scripts/hearts-logreg-scaled.py")

        elif choice == "6":
            run_script("scripts/hearts-knn.py")

        elif choice == "7":
            run_script("scripts/hearts-tree.py")

        elif choice == "8":
            run_script("scripts/hearts-rf.py")

        elif choice == "9":
            run_script("scripts/hearts-diagnose.py")     


        elif choice == "e":
            print("> Exiting...")
            break

        else:
            print("> Invalid input")

        print()

# Start
# -------------------------
main() if __name__ == "__main__" else None