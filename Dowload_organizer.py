import os 
import shutil

download_path = os.path.join(os.path.expanduser("~"), "Downloads")

folders = {"Images": ["jpg","png"],
           "Documents": ["pdf","txt"],
           "Videos": ["mp4"],
              "Music": ["mp3"],}

for folder in folders:
    folder_path = os.path.join(download_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
        
        for file in os.listdir(download_path):
            file_path = os.path.join(download_path,file)
            print(f"Processing file: {file_path}")
            
            if os.path.isfile(file_path):
                for folder, extensions in folders.items():
                    if file.split(".")[-1].lower() in extensions:
                        shutil.move(file_path, os.path.join(download_path, folder))
                        print(f"Moved file: {file_path} to {folder}")
                        break
                    
                    
