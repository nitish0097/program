class Notes:
    def __init__(self):
        self.Notes = {}
    def addtitle(self,title,content):
        self.Notes[title] = self.Notes.get(title,[content])
    def process(self):
        n = int(input("enter the number 1  for writting content and 2 for retriving the  data"))
        if n == 1:
            def addtitle(title, content):
                self.Notes[title] = self.Notes.get(title, [content])
            addtitle(input("enter the title :"), input("enter the content:"))
        if n==2:
            print self.Notes   # it prints the dictionay
            for a in enumerate(self.Notes,0): #it  get the index for  keys-valuespairs
                print a
            self.Notes.items()
            d = [(k, v) for k, v in self.Notes.items()]  # converts into list
            i=int(input("enter the number for retriving the data"))
            print d[i]

o = Notes()
o.addtitle(input("enter the title"),input("enter the content"))
o.process()

