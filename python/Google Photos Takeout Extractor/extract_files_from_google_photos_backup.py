"""
Author: Luis Rodriguez Chaves
Beggining date: 12-1-25
File to extract images from directory recursively. This script moves all images or videos into a new directory next to the original of Google Photos. It just ignores the jsons.
Python version used: 3.13
Takedown directory must be first extracted with all it's parts before running this script.
Version: 2.0
"""
import os
from pathlib import Path
import traceback
import datetime
import shutil

def generate_request_to_google_photos_directory():
    input_user="invalid"
    while input_user=="invalid":
        input_user=input("Do you wish to copy the files to a new backup directory? (Y/N) ")
        input_user=input_user.upper()
        if input_user not in ["Y","N"]:
            input_user="invalid"
            print("Input invalid")
    
    current_directory=input("Please input the address where the Google Photos backup is: ")
    #current working directory
    if "Google Fotos" or "Google Photos" in os.listdir(Path(current_directory)):
        alternatives_dir=["Google Fotos","Google Photos"]
        for alternative in alternatives_dir:                
            try:
                google_photos_directory_=f"{current_directory}\\{alternative}\\"
                print(f"Google Directory found: {google_photos_directory_}\n")
                if input_user=="Y":
                    copy_google_photos_directory(google_photos_directory=google_photos_directory_,cwd=current_directory)
                    print("Backup successful!")
                    return
                elif input_user=="N":
                    print("Backup aborted")
                    return
                else:
                    return
            except:
                print(traceback.format_exc())
        return
    else:
        print("This directory is not usable by this program, please move this script to a directory with a Google Photos directory inside")
        return
    
def copy_google_photos_directory(google_photos_directory,cwd):
    """
        Copy all files of pictures to another directory if found.
    """
    try:     
        files_to_copy_to_new_directory=[]
        for root,dirs,files in os.walk(top=Path(google_photos_directory)):
            for file in files:
                if ".json" not in file:
                    files_to_copy_to_new_directory.append(Path(f"{root}\\{file}"))
        
        #verification files where actually found and it's not empty
        if not files_to_copy_to_new_directory:
            print(f"files_to_copy_to_new_directory: {files_to_copy_to_new_directory}")
            raise Exception("No files to copy")
        
        #directory generations
        files_to_copy_to_new_directory=files_to_copy_to_new_directory
        date_=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        new_directory_address=f"{cwd}\\GooglePhotos_recovery_copy_{date_}"
        new_directory_name=f"GooglePhotos_recovery_copy_{date_}"
        os.makedirs(Path(new_directory_address))
        print(f"New directory {new_directory_name} created")
        
        counter=1
        number_of_files_to_copy=len(files_to_copy_to_new_directory)
        for file in files_to_copy_to_new_directory:
            percentage=round(counter/number_of_files_to_copy*100)
            print(f"Progress: {counter}/{number_of_files_to_copy} ({percentage}%)", end="\r")
            shutil.copy2(src=file,dst=new_directory_address)
            counter+=1
        print(f"Files transfered to {new_directory_address}")
        return
    except:
        raise

generate_request_to_google_photos_directory()