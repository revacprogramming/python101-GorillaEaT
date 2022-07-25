

class Menu:
    def __init__(self):
        self.l=[]
    def add(self,item,price):
        self.l.append((item,price))
    def show(self):
        for a,b in self.l: print(a,b)

m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)
m.add("chutney",30)
m.add("dosa",40)
m.show()
