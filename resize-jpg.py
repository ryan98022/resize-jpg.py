import os
import sys
from PIL import Image

#  This program walkes a folder tree and searches it recursively
#  and down-sizes jpg files to under 3 MB's. Genreally 1-2 MBs.
#  all other files (mp4, gif, etc) just get a copy made.
#  after, you should have a 'small' directory in the directory
#  you ran it in with a smaller version of all your jpg's in a mirrored
#  folder tree.
#  You can add a target folder as an argument or just run this in the
#  target folder.

THRESHOLD = 3
OKFT = ['.jpg', '.jpeg'] #Ok File Types
MB = 1024 * 1024
#check if argument was supplied and if its valid.
if len(sys.argv) > 1:
    if not os.path.isdir(sys.argv[1]):
        print("Whatever argument you entered is not a valid Directory.")
        exit()
    else:
        Root_Source = sys.argv[1]
else:
    # No dir supplied, go with the dir we're in.
    Root_Source = os.getcwd()

Root_Dest = os.path.join(Root_Source, "small")

if os.path.isdir(Root_Dest):
    print("Target dir:  " + Root_Dest + " already exists.  Please rename or delete and try again.")
    exit()


tree = os.walk(Root_Source)

Num_of_Files = 0
Index = 1
directory = []
for item in tree:
    Num_of_Files += len(item[2])
    directory.append(item)
print("Your root directory is: " + Root_Source)
print(str(Num_of_Files) + " files in this Directory tree.")
def ok():
    while True:
        look_good = input("Does this look right to you? (Y)es/(N)o:  ")
        if look_good.lower() == "y":
            break
        elif look_good.lower() == "n":
            print("Exiting.")
            print("If your root directory is wrong, either you entered it wrong, or you are in the wrong directory")
            exit()
        else:
            print("Y and N are the only recognized answers.  Try again.")

ok()

os.mkdir(Root_Dest)

def get_ratio(size):
    if size < THRESHOLD:
        factor = 100 
    elif size < THRESHOLD + 1:
        factor = 95 
    elif size < THRESHOLD + 2:
        factor = 90
    elif size < THRESHOLD + 3:
        factor = 85
    else:
        factor = 80
    return factor

def process(read, write):
        stats = os.stat(read)
        with Image.open(read) as img:
          q = get_ratio(int(stats.st_size)/MB)
          if (q != 100):
              img.save(write, quality=q, optimize=True)
          else:
              img.save(write)

for x in directory:
    stub = x[0].replace(Root_Source, '')
    if stub:
        os.mkdir(os.path.join(Root_Dest, stub))
    if x[2]:
        print(str(len(x[2])) + " files in folder:  " + x[0])
        for file in x[2]:
            if any(m in file.lower() for m in OKFT):
                print("Processing file :  " + file + " " + str(Index) + " of " + str(Num_of_Files))
                Index += 1
                source = os.path.join(x[0], file)
                dest = os.path.join(Root_Dest, stub, "small-" + file)
                process(source, dest)
                
            else:
                print("Copying file unchanged:  " + file + " " + str(Index) + " of " + str(Num_of_Files))
                Index += 1
                source = os.path.join(x[0], file) 
                dest = os.path.join(Root_Dest, stub, file)
                string = "cp " + source + " " + dest
                os.system(string)

