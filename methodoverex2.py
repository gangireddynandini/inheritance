#multilevelex.py of same methods different body
class circle:
    def draw(self):
        print("drawing circle")
class square(circle):
    def draw(self):

        print("draw square")
class rect(square):
    def rect(self):
        circle.draw(self)
        square.draw(self)
        print("draw rect")
r=rect()
r.rect()