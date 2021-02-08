# Copy to Location
Script for copying files from a source location to a destination

Uses command line arguments to select source folder, destination folder, and file types. If any arguments are not provided, will use
easygui to allow users to select missing arguments. 

Copies files from source folder to destination folder if the files are of the selected file type and do
not exist at the destination location. Does not copy folders inside of source folder. Currently runs once immediately and 
then again every 20 seconds. 

Simply run copy_to_location.py and follow the instructions.

I created this script because my employer is copying audio recordings from individual computers to a network storage location
and I wanted practice automating the process. This should work for network locations, but I have not tested it as of yet, so that'll 
be in the next update. I'll probably also add the ability to retrieve settings from a file, and user-selected
loop time.
