class Notes:
    def __init__(self):
        self.Notes = {}
    def process(self):
      while True:
        n = int(input("enter the number 1  for writting content and 2 for retriving the  data"))
        if n == 1:
            def addtitle(title, content):
                self.Notes[title] = self.Notes.get(title, [content])
<<<<<<< HEAD
            addtitle(raw_input("enter the title :"),raw_input("enter the content:"))
        elif n==2:
          if self.Notes == {}:
            def addtitle(title,content):
              self.Notes[title] = self.Notes.get(title, [content])
            addtitle(raw_input("enter the title :"), raw_input("enter the content:"))
            print (self.Notes)   # it prints the dictionay
          else:
            for a in enumerate(self.Notes,0): #it  get the index for  keys-valuespairs
                print (a)
=======
            addtitle(input("enter the title :"), input("enter the content:"))
        if n==2:
            print self.Notes   # it prints the dictionay
            for a in enumerate(self.Notes,0): #it  get the index for  keys-valuespairs
                print a
>>>>>>> e5d513f6a71f827ba5576604896544e403dc6637
            self.Notes.items()
            d = [(k, v) for k, v in self.Notes.items()]  # converts into list
            i=int(input("enter the number for retriving the data"))
            print (d[i])

o = Notes()
o.process()