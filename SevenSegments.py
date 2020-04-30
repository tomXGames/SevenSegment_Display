from Segment import Segment

class SevenSegments:
    margin = 20
    seg = Segment(0, 0, 0, False)
    pos = [[],[],[],[],[],[],[]]
    number = 0,
    def __init__(self, num):
        number = num
        self.pos = [[self.seg.w+(2*self.margin), self.margin, 90], 
        [self.pos[0][0] + self.seg.h+self.margin, 2*self.margin+self.seg.w, 0], 
        [self.pos[0][0] + self.seg.h+self.margin, 3*self.margin+self.seg.w+self.seg.h, 0], 
        [self.pos[0][0], self.pos[2][1]+self.margin+self.seg.w, 90], 
        [self.margin, 3*self.margin+self.seg.w+self.seg.h, 0],
        [self.margin, 2*self.margin+self.seg.w, 0],
        [self.seg.w +2*self.margin, self.seg.h+self.seg.w+2*self.margin, 90]]
        
    def update(self):
        for i in self.pos:
            s = seg(self.pos[i][0], self.pos[i][1], self.pos[i][2], True)
            s.show()
            
    
