import os
import shutil

files = os.listdir()

for file in files:
    if file.endswith(".txt"):
        os.makedirs("Texts", exist_ok=True)
        shutil.move(file,"Texts/" + file)