class circle:
    def __init__(self,r):

        ar=3.14*(r**2)
        print("area of a circle:",ar)
class square:
    def __init__(self,s):

        ars=s*s
        print("area of a square:", ars)

class rect(square,circle):
    def __init__(self,l,b):


        arr=l*b
        print("area of a rectangle:", arr)
        super().__init__(int(input("enter side:")))
        circle.__init__(self,int(input("enter radius")))
l=int(input("enter length:"))
b=int(input("enter bredth:"))
r=rect(l,b)



