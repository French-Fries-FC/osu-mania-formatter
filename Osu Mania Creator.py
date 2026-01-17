from pathlib import Path
import time
import os

PROGRAM_VERSION = "1.0.0"
PROJECT_NAME = "Operation New Seas"
PROJECT_DATE = "20260116"

FILE_DIR = Path(__file__).parent

Output_dir = FILE_DIR / "osuManiaFormatter" / "skin.ini"
keyNum = 4

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_path(path: str) -> str:
    try:
        s = 0
        for char in path:
            if char == "\\":
                path = path.replace("\\", "/")
                s += 1
            if s == 8:
                c = path.split("/", 8)
        return c[8]
    except Exception as e:
        print("Error loading path:", e)

def take_image(prompt="Drag a PNG into the terminal and press Enter:"):
    while True:
        print(prompt)
        path_str = input("> ").strip()

        path = Path(path_str)

        if not prompt == "":
            if not path.exists():
                print("File does not exist. Check the file path again.")
            elif path.suffix.lower() != ".png":
                print("Not a PNG file")
                con_op = input("Continue? (y/n): ").strip().lower()
                if con_op != 'y':
                    clear_console()
                    print("Select a new file.")
                    continue
                else:
                    print("Loading image...")
                    rel_path = clean_path(str(path))
                    return rel_path
            else:
                print("Loading image...")
                rel_path = clean_path(str(path))
                return rel_path
        else:
            print("Loading no image...")
            return None

def locate_dump():
    print("File directory: ", FILE_DIR), time.sleep(.1)
    print("Locating dump folder..."), time.sleep(.7)
    if not (FILE_DIR / "osuManiaFormatter").exists():
        print("Dump folder not found. Creating dump folder..."), time.sleep(.7)
        (FILE_DIR / "osuManiaFormatter").mkdir()
    else:
        print("Dump folder found."), time.sleep(.2)
    if not (FILE_DIR / "osuManiaFormatter" / "skin.ini").exists():
        open(FILE_DIR / "osuManiaFormatter" / "skin.ini", "x").close()
        print("skin.ini created!")
    print("Loaded skin.ini at: " + (str(Output_dir)))


print("Welcome to Osu! Mania Formatter.")
print("By French Fries")
print("Version:", PROGRAM_VERSION, "-", PROJECT_NAME, PROJECT_DATE, "\n")
locate_dump()

with open(Output_dir, "w") as f:
    f.write("[Mania]\n\n")

print("\nOptions: \n[0] New Image\n[1] New Settings\n[2] New Keys")
option = input("> ").strip()

if option == "0" or option == "1":
    print("\nMode:\n[0] Easy\n[1] Advanced")
    mode = input("> ").strip()

clear_console()
print("How many keys?")
k = input("> ").strip()
keyNum = int(k)

with open(Output_dir, "a") as f:
    # Key Counts
    f.write("    Keys: " + str(keyNum) + "\n\n")

    if option == "0" or option == "1":
        print("[Settings]\n")

        # Upside Down
        e_upsidedown = input("UpsideDown: ").strip()
        f.write("    UpsideDown: " + e_upsidedown + "\n")

        # Barline Height
        e_bar = input("BarlineHeight: ").strip()
        f.write("    BarlineHeight: " + e_bar + "\n")

        # Column Start
        e_colStart = input("ColumnStart: ").strip()
        f.write("    ColumnStart: " + e_colStart + "\n")

        # Column Right
        e_colRight = input("ColumnRight: ").strip()
        f.write("    ColumnRight: " + e_colRight + "\n")

        # Column Spacing
        e_colSpacing = input("ColumnSpacing: ").strip()
        f.write("    ColumnSpacing: " + e_colSpacing + "\n")

        # Column Line Width (multi-mode)
        if mode == "1":
            f.write("    ColumnLineWidth: ")
            for count in range(keyNum + 1):
                e_colLineWid = input(f"ColumnLineWidth{count}: ").strip()
                f.write(e_colLineWid + ",")
            f.write("\n")
        else:
            e_colLineWid = input("ColumnLineWidth: ").strip()
            temp_string = f"{e_colLineWid},{e_colLineWid},{e_colLineWid},{e_colLineWid}"
            f.write("    ColumnLineWidth: " + temp_string + "\n")

        # Column Width (multi-mode)
        if mode == "1":
            f.write("    ColumnWidth: ")
            for count in range(keyNum + 1):
                e_colWid = input(f"ColumnWidth{count}: ").strip()
                f.write(e_colWid + ",")
            f.write("\n")
        else:
            e_colWid = input("ColumnWidth: ").strip().strip()
            temp_string = f"{e_colWid},{e_colWid},{e_colWid},{e_colWid},{e_colWid}"
            f.write("    ColumnWidth: " + temp_string + "\n")

        f.write("\n")

        # Combo Position
        e_comboPos = input("ComboPosition: ").strip()
        f.write("    ComboPosition: " + e_comboPos + "\n")

        # Hit Position
        e_hitPos = input("HitPosition: ").strip()
        f.write("    HitPosition: " + e_hitPos + "\n")

        # Score Position
        e_scorePos = input("ScorePosition: ").strip()
        f.write("    ScorePosition: " + e_scorePos + "\n")

        f.write("\n")

        # Judgement Line
        e_judLine = input("JudgementLine: ").strip()
        f.write("    JudgementLine: " + e_judLine + "\n")

        # Keys Under Notes
        e_keyUndNote = input("KeysUnderNotes: ").strip()
        f.write("    KeysUnderNotes: " + e_keyUndNote + "\n")

        # Note Body Style
        e_noteBodSty = input("NoteBodyStyle: ").strip()
        f.write("    NoteBodyStyle: " + e_noteBodSty + "\n")

        f.write("\n")

    if option == "0" or option == "2":
        print("\n[Images]\n")

        # Key Images
        for count in range(keyNum):
            temp_img = take_image(f"KeyImage{count}")
            f.write(f"    KeyImage{count}: " + str(temp_img) + "\n")
            temp_img = take_image(f"KeyImage{count}D")
            f.write(f"    KeyImage{count}D: " + str(temp_img) + "\n")
            f.write("\n")

        print("Keys loaded!\n")

        # Note Images
        for count in range(keyNum):
            temp_img = take_image(f"NoteImage{count}")
            f.write(f"    NoteImage{count}: " + str(temp_img) + "\n")
            temp_img = take_image(f"NoteImage{count}H")
            f.write(f"    NoteImage{count}H: " + str(temp_img) + "\n")
            temp_img = take_image(f"NoteImage{count}L")
            f.write(f"    NoteImage{count}L: " + str(temp_img) + "\n")
            temp_img = take_image(f"NoteImage{count}T")
            f.write(f"    NoteImage{count}T: " + str(temp_img) + "\n")
            f.write("\n")

        print("Notes loaded!\n")

        # Stage Images
        i_stageL = take_image(f"Stage Left")
        f.write(f"    StageLeft: " + str(i_stageL) + "\n")
        i_stageR = take_image(f"Stage Right")
        f.write(f"    StageRight: " + str(i_stageR) + "\n")
        i_stageH = take_image(f"Stage Hint")
        f.write(f"    StageHint: " + str(i_stageH) + "\n")

        print("Stage loaded!\n")