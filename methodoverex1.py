class circle:
    def draw(self):
        print("drawing circle")
class square(circle):
    def draw(self):
        super().draw()
        print("draw square")
class rect(square):
    def rect(self):
        super().draw()
        print("draw rect")
r=rect()
r.rect()