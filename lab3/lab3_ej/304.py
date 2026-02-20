class StringHandler :
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

ww = StringHandler()
ww.getString()
ww.printString()
        