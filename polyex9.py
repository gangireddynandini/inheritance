class circle:
    def __init__(self,r):

        ar=3.14*(r**2)
        print("area of a circle:",ar)
class square(circle):
    def __init__(self,s):

        ars=s*s
        print("area of a square:", ars)

class rect(square):
    def __init__(self,l,b):


        arr=l*ba
        print("area of a rectangle:", arr)
        super().__init__(2)
        circle.__init__(self,3)
r=rect(2,3)



