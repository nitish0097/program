class Notes:
    def __init__(self):
        self.Notes = {}

    def process(self):
        n = int(input("enter the number 1  for writting content and 2 for retriving the  data"))
        if n == 1:
            def addtitle(title, content):
                self.Notes[title] = self.Notes.get(title, [content])
        addtitle(input("enter the title :"), input("enter the content:"))
        n==2:
            print self.Notes #it prints the dictionay
            self.Notes.items()
            d = [(k,v) for k,v in self.Notes.items()]#converts into list
            for a, b in enumerate(d,0): #it  get the index for  keys-valuespairs
                print a, b
                i=int(input("enter the number for retriving the data"))
                print d[i]

o = Notes()
o.process()
