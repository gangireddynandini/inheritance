class circle:
    def __init__(self):
        r=int(input("enter radius:"))
        ar=3.14*(r**2)
        print("area of a circle:",ar)
class square(circle):
    def __init__(self):
        s=int(input("enter side:"))
        ars=s*s
        print("area of a square:", ars)

class rect(square):
    def __init__(self):
        self.l=int(input("enter length:"))
        b=int(input("enter breadth:"))
        arr=self.l*b
        print("area of a rectangle:", arr)
        super().__init__()
        circle.__init__(self)
r=rect()



