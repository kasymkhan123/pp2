import os
import shutil
# copy file
shutil.copy("example/test.txt", "example/folder/test_copy.txt")
# move file
shutil.move("example/test.txt", "example/folder/subfolder/test.txt")