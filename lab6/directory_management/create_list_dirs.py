import os
# create directories
os.makedirs("example/folder/subfolder", exist_ok=True)
# create file
with open("example/test.txt", "w") as f:
    f.write("Hello")
# list files 
print(os.listdir("example"))
# find txt files
for root, dirs, files in os.walk("example"):
    for file in files:
        if file.endswith(".txt"):
            print("Found:", os.path.join(root, file))
