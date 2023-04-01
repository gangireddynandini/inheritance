
class grandparent:
    def getgpprop(self):
        self.gpp=float(input("ENTER GRAND PARENT PROPERTY:"))
class parent(grandparent):
    def getpprop(self):
        self.pp=float(input("enter parent property:"))
class child(parent):
    def childprop(self):
        self.cprop=float(input("enter child property:"))

    def totalprop(self):
        #global prop
        self.getgpprop()
        self.getpprop()
        self.childprop()
        prop= self.gpp+self.pp+self.cprop

        print("total property belongs to child:",prop)
c=child()
c.totalprop()
