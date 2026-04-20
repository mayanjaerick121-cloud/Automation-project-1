import os
for file in os.listdir():
    if file.endswith(".txt"):
        new_name = "note_" + file
        os.rename(file, new_name) 