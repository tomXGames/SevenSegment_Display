class Segment():
    w = 10
    h= 50
    x = 0
    rotation =False;
    y=0

    
    def __init__(self, x, y, rotation, on):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.on = on;

    
    def show(self):
        push()
        if (self.on):
            fill(color(255,0,0))
            if(self.rotation):
                rect(self.x,self.y,self.h, self.w)
            else:
                rect(self.x,self.y,self.w, self.h)
        else:
           pass
        pop()
