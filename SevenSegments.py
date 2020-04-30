from Segment import Segment

class SevenSegments:
    margin = 20
    pos = [[Segment.w+(2*margin), margin, 90], 
        [self.pos[0][0] + Segment.h+self.margin, 2*self.margin+Segment.w, 0], 
        [self.pos[0][0] + Segment.h+self.margin, 3*self.margin+Segment.w+Segment.h, 0], 
        [self.pos[0][0], self.pos[2][1]+self.margin+Segment.w, 90], 
        [self.margin, 3*self.margin+Segment.w+Segment.h, 0],
        [self.margin, 2*self.margin+Segment.w, 0],
        [Segment.w +2*self.margin, Segment.h+Segment.w+2*self.margin, 90]]
    number = 0,
    def __init__(self, num):
        number = num

    def update(self):
        for i in self.self.pos:
            s = Segment(self.pos[i][0], self.pos[i][1], self.pos[i][2], True)
            s.show()
            
    
