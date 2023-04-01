class circle:
    def area(self):
        r=int(input("enter radius:"))
        ar=3.14*(r**2)
        print("area of a circle:",ar)
class square(circle):
    def area(self):
        s=int(input("enter side:"))
        ars=s*s
        print("area of a square:", ars)

class rect(square):
    def area(self):
        self.l=int(input("enter length:"))
        b=int(input("enter breadth:"))
        arr=self.l*b
        print("area of a rectangle:", arr)
        super().area()
        circle.area(self)
r=rect()
r.area()


