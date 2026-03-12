# create file
with open("data.txt", "w") as f:
    f.write("You will never walk alone\nLiverpool<3\n")
# read file
with open("data.txt") as f :
    print(f.read())
