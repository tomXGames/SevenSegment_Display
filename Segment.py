class Segment():
    w = 10
    h= 50
    x = 0
    rotation =0;
    y=0
    on = False
    
    def __init__(self, x, y, rotation, on):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.on = on;
    
    def show(self):
        if self.on:
            fill(color(255,0,0))
        else:
            noFill()
        push()
        rotate(self.rotation)
        rect(self.x,self.y,self.w, self.h)
        pop()
