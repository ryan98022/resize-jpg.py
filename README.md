# resize-jpg.py
Automated script for down scaling large numbers of jpg files to conserve space on phone/icloud.

Accepts an argumet for entry point directory or will assume your current directory is the entry point.

$ python3 resize-jpg.py /path/to/photo/folder

OR

/path/to/photo/folder$ python3 resize-jpg.py

Either will result in /path/to/photo/folder/small/(mirror folder tree with smaller MB versions of all your jpgs)

Files not ending with jpg or jpeg will just be copied into respective folders for easy uploading.  No file type logic
is used.  If its not jpg or jpeg, it make a copy.  It asusmes you still want mp4, gif, png, etc files in the same relative
location.

All source jpg's at or below the THRESHOLD size just get copied as well.  Default THRESHOLD is 3MB.  Adjust as you see fit.
