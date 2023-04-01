class grandparent:
    def getgpprop(self):
        self.gpp=float(input("ENTER GRAND PARENT PROPERTY:"))
class parent(grandparent):
    def getpprop(self):
        self.pp=float(input("enter parent property:"))
class child(parent):

    def childprop(self):
        self.cprop=float(input("enter child property:"))
    def totalproperty(self):
        prop=self.gpp+self.pp+self.cprop
        print("properties of child")
        print("grand parent properties:{}".format(self.gpp))
        print(" parent properties:{}".format(self.pp))
        print("child properties:{}".format(self.cprop))
        print("child properties:{}".format(prop))
co=child()
co.childprop()
co.getpprop()
co.getgpprop()
co.totalproperty()





