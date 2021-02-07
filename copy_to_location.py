import os
from easygui import *
from shutil import copyfile
from time import perf_counter

intro_text = """
Welcome to the file copy/backup utility. 
You may exit early by pressing a cancel button before the final step.
"""

"""Cleans contents of source_folder by removing folders, 
files that exist at the destination, 
and files with unapproved file types."""
def clean_contents(source_folder, source_contents, destination_contents, file_types = None):
    cleaned_contents = [] # list for appending approved files
    
    for file in source_contents:
        if os.path.isdir(os.path.join(source_folder, file)) == True: # if file is a folder, do not add
            pass
        elif file in destination_contents: # if file already exists at destination, do not add
            pass
        elif file_types:
            filename, file_ext = os.path.splitext(file) # split file into filename and extension
            if file_ext[1:] not in file_types: # if extension, starting one character past dot, is not an approved file_type, do not add
                pass 
            else: 
                cleaned_contents.append(file) # if the file passed all of the checks, add it to cleaned_contents
    
    return cleaned_contents # return approved files

def file_types_check(file_types):
    for type in file_types:
        if type.isalpha() != True:
            msgbox("You used an invalid character in your file types, probably a period. Please try again.")
            return False
        else: 
            pass
        return True


msgbox(intro_text) # user-friendly program description
msgbox("Select a source folder") # user-friendly direction
source_folder = diropenbox("Select a source folder...") # user selects source_folder
if source_folder == None: # if user pressed cancel, exit program
    exit()

msgbox("Select a destination folder") # user-friendly direction
destination_folder = diropenbox("Select a destination folder...") # user selections destination_folder
if destination_folder == None: # if user pressed cancel, exit program
    exit()

choices = ('All Files', 'Pick File Types') # choices for upcoming button box
decision = buttonbox("Would you like to copy all files, or pick specific file types?",
                     "Select One", choices) # user clicks 'all files' or 'pick files' button
if decision == "All Files": # if they picked all files
    file_types = 'all'
elif decision == "Pick File Types": # if they picked pick files
    instructions = """Enter the file extensions you would like copied, separated by spaces. 
Only enter alphabetic characters, no punctuation.
Good Example: jpg png gif
Bad Example: .jpg .png .gif"""
    clean_input = False
    while clean_input == False:
        file_types = enterbox(instructions)
        file_types = file_types.split() # splits user entered file types into list of file types
        clean_input = file_types_check(file_types)    
else: 
    quit()


time_stamp = perf_counter()
first_run = False

msgbox("Program will now run in the background.")
while True:
    if first_run == False:
        source_contents = os.listdir(source_folder)
        destination_contents = os.listdir(destination_folder)
        if file_types != 'all': # if they picked file types
            cleaned_contents = clean_contents(source_folder, source_contents, destination_contents, file_types)
        else: # if they selected all files
            cleaned_contents = clean_contents(source_folder, source_contents, destination_contents)
        for file in cleaned_contents:
            copyfile(os.path.join(source_folder, file), os.path.join(destination_folder, file))
        first_run = True
    
    else:
        if perf_counter() - time_stamp > 20: # 10800 is every 3 hours
            source_contents = os.listdir(source_folder)
            destination_contents = os.listdir(destination_folder)
            if file_types != 'all': # if they picked file types
                cleaned_contents = clean_contents(source_folder, source_contents, destination_contents, file_types)
            else: # if they selected all files
                cleaned_contents = clean_contents(source_folder, source_contents, destination_contents)
            for file in cleaned_contents:
                copyfile(os.path.join(source_folder, file), os.path.join(destination_folder, file))
            time_stamp = perf_counter() # reset time stamp

