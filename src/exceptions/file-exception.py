from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent.parent

file_path=BASE_DIR/"file.txt"

try:
    with open(file_path,"r") as f:
        file_data=f.read()
        print(file_data)
        
except FileNotFoundError as fne:
    print(fne)
except FileExistsError as fee:
    print(fee)
except Exception as e:
    print(e)
finally:
    print("Done File Operation")