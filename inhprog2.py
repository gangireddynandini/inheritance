class c1:
    def seta(self):
        self.a=10
class c2(c1):
    def setb(self):
        self.b=20
        self.seta()
        self.disp()
    def disp(self):
        print("value of a(c1-bc):{}".format(self.a))
        print("value of b(c2-bc):{}".format(self.b))
o2=c2()
print("content of c2:",o2.__dict__)
o2.setb()