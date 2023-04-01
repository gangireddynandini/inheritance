#multilevelex.py of same methods different body
class circle:
    def __init__(self):
        print("drawing circle")
class square(circle):
    def __init__(self):

        print("draw square")
class rect(square):
    def __init__(self):
        circle.__init__(self)
        square.__init__(self)
        print("draw rect")
r=rect()
