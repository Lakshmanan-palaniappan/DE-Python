from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent.parent

file_path=BASE_DIR/"file.txt"
print(file_path)
with open(file_path,"w",encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")

with open(file_path,"r",encoding="utf-8") as f:
    lines=f.seek(3)
    print(f.tell())
print(lines)