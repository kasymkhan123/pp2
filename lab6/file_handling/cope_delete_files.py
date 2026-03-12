import os
import shutil
# copy file
shutil.copy("data.txt", "backup.txt")
# delete file 
if os.path.exists("backup.txt"):
    os.remove("backup.txt")