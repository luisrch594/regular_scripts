"""
Author: Luis Rodriguez Chaves
Beggining date: 12-1-25
File to extract images from directory recursively. This script moves all images or videos into a new directory next to the original of Google Photos. It just ignores the jsons.
Python version used: 3.13
Takedown directory must be first extracted with all it's parts before running this script.
"""
import os
from pathlib import Path
import traceback
import datetime
import shutil

def generate_request_to_google_photos_directory():
    current_directory=os.getcwd()
    #current working directory
    if "Google Fotos" or "Google Photos" in os.listdir(current_directory):
        try:
            google_photos_directory_=f"{current_directory}\\Google Fotos\\"
            print(f"Google Directory found: {google_photos_directory_}\n")
            copy_google_photos_directory(google_photos_directory=google_photos_directory_,cwd=current_directory)
            return
        except:
            print(traceback.format_exc())
        
        try:
            google_photos_directory_=f"{current_directory}\\Google Photos\\"
            print(f"Google Directory found: {google_photos_directory_}\n")
            copy_google_photos_directory(google_photos_directory=google_photos_directory_,cwd=current_directory)
            return            
        except:
            print(traceback.format_exc())
        
        return
    else:
        print("This directory is not usable by this program, please move this script to a directory with a Google Photos directory inside")
        return
    
def copy_google_photos_directory(google_photos_directory,cwd):
    """
        Move all files of pictures to another directory if found.
    """
    try:     
        files_to_copy_to_new_directory=[]
        for root,dirs,files in os.walk(top=Path(google_photos_directory)):
            for file in files:
                if ".json" not in file:
                    files_to_copy_to_new_directory.append(Path(f"{root}\\{file}"))
        
        #verification files where actually found and it's not empty
        if not files_to_copy_to_new_directory:
            raise Exception("No files to copy")
        
        #directory generations
        date_=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_directory_address=f"{cwd}\\GooglePhotos_recovery_{date_}"
        new_directory_name=f"GooglePhotos_recovery_{date_}"
        os.makedirs(Path(new_directory_address))
        print(f"New directory {new_directory_name} created")
        
        counter=1
        number_of_files_to_copy=len(files_to_copy_to_new_directory)
        for file in files_to_copy_to_new_directory:
            percentage=round(counter/number_of_files_to_copy*100)
            print(f"Progress: {counter}/{number_of_files_to_copy} ({percentage}%)", end="\r")
            shutil.copy2(file,new_directory_address)
            counter+=1
        print(f"Files transfered to {new_directory_name}")
        return
    except:
        raise


generate_request_to_google_photos_directory()