"""
Author: Luis Rodriguez Chaves
Beggining date: 12-1-25
This script will adquire any file in the indicated folder by the user, and then sort it by year(using last modified date), creating a folder for each year and month.
This script can be improved to sort by day but the functionality I require only needs to sort by year and month.
It ignores directories. Can be useful for sorting images of all sorts.

Possible improvements:
Add posibility to handle folders.
Add feature to handle by creation date or last modification date.

Python version used: 3.13

Version: 2.0
"""
import os
from pathlib import Path
import traceback
import datetime
import shutil
import time


from tkinter.filedialog import askdirectory
import shutil

class GUI_prompt():
    def __init__(self):
        self._initializeWindow()

    def _initializeWindow(self):      
        #select folder to sort
        folder_path = askdirectory(title='Select Folder to sort')


        #variables of new folder and context
        parent_folder_path=Path(folder_path).parent
        new_folder_name="sorted_"+Path(folder_path).name
        print(f"new_folder_name: {new_folder_name}")

        self._create_parent_directory(parent_folder_path=parent_folder_path,new_folder_name=new_folder_name,src=folder_path)

        
    def _create_parent_directory(self,parent_folder_path,new_folder_name,src):
        #create new folder
        try:
            address_to_new_folder=Path(str(parent_folder_path)+"\\"+new_folder_name)
            if address_to_new_folder.exists():
                recreate_directory_="invalid"

                while recreate_directory_=="invalid_input":
                    recreate_directory_=input(f"Do you wish to delete previous directory {new_folder_name}? (Y=Recreate directory entirely/N=Add missing files and preserve repeated files): ")
                    recreate_directory_=recreate_directory_.upper()
                    if recreate_directory_ in ["Y","N"]:
                        if recreate_directory_=="N":
                            self.execute_necessary_file_movements(src_folder=src,address_to_new_folder=address_to_new_folder)
                        elif recreate_directory_=="Y":
                            self.delete_directory(address_to_new_folder)
                            self.execute_necessary_file_movements(src_folder=src,address_to_new_folder=address_to_new_folder)
                    else:
                        recreate_directory_="invalid_input"
                    
            else:
                address_to_new_folder.mkdir()
                self.execute_necessary_file_movements(src_folder=src,address_to_new_folder=address_to_new_folder)
        except:
            print(traceback.format_exc())
            raise("Error Found - Folder exists already or is unable to write")        
        

    def execute_necessary_file_movements(self,src_folder,address_to_new_folder):
        """
        This will create a directory if it is requested
        """
        for root,dirs,files in os.walk(top=Path(src_folder)):
            number_of_files_to_copy=len(files)
            counter=1
            for file in files:
                #obtain time in seconds and convert it to human format

                src=str(Path(f"{root}\\{file}"))

                modification_date=f"{time.ctime(os.path.getmtime(src))}"
                #convert it into a timestamp
                t_obj = time.strptime(modification_date)
                #get year, month and day of file
                year_m_date=time.strftime("%Y", t_obj)
                month_m_date=time.strftime("%B", t_obj)
                #this can be used later on for improvements.
                #day_c_date=time.strftime("%A", t_obj)

                #create new directory if it doesn't exist, it will create also intermediate directories if necessary
                destiny_folder=f"{address_to_new_folder}\\{year_m_date}\\{month_m_date}"
                if not os.path.exists(Path(destiny_folder)):
                    os.makedirs(Path(destiny_folder))

                if os.path.exists(Path(f"{destiny_folder}\\{file}")):
                    #ignore this file if it already exists
                    continue
                else:
                    shutil.copy2(src=src,dst=destiny_folder)

                #print progress of file transfer
                percentage=round(counter/number_of_files_to_copy*100)
                print(f"Progress: {counter}/{number_of_files_to_copy} ({percentage}%)", end="\r")
                counter+=1

        print("File transfer and sorting successfull")

    def delete_directory(self,path):
        shutil.rmtree(path)


app=GUI_prompt()