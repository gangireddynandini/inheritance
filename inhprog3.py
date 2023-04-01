class grandparent:
    def getgpprop(self):
        self.gpp=3.4
class parent(grandparent):
    def getpprop(self):
        self.pp=13.4
class child(parent):

    def childprop(self):
        self.cprop=4
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





