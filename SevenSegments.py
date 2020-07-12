#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from Segment import Segment

class SevenSegments:
    chars=  {
    "0": 0b00111111,
    "1": 0b00000110,
    "2": 0b01011011,
    "3": 0b01001111,
    "4": 0b01100110,
    "5": 0b01101101,
    "6": 0b01111101,
    "7": 0b01111101,
    "8": 0b01111111,
    "9": 0b01101111,
    " ": 0b00000000,
    "A": 0b01110111,
    "B": 0b01111100,
    "C": 0b00111001,
    "D": 0b01011110,
    "E": 0b01111001,
    "T": 0b01111000,
    "F": 0b01110001,
    "G": 0b00111101,
    "N": 0b01010100,
    "H": 0b01110110,
    "I": 0b00110000,
    "J": 0b00011110,
    "L": 0b00111000,
    "O": 0b01011100,
    "P": 0b01110011,
    "R": 0b01010000,
    "S": 0b01101101,
    "U": 0b00111110,
    " ": 0b00000000,
    } 
    x = 0
    margin = 20
    seg = Segment(0, 0, 0, False)
    pos = [[],[],[],[],[],[],[]]
    number = 0x00
    SegmentW = 2*seg.w + seg.h + 4*margin
    SegmentH = 2*seg.h + 2* seg.w + 6*margin
    
    def __init__(self, num, x):
        self.number = self.chars.get(num.upper())
        self.x = x 
        self.pos = [[self.seg.w+(2*self.margin), self.margin, True], 
        [self.seg.w+(2*self.margin) + self.seg.h+self.margin, 2*self.margin+self.seg.w, False], 
        [self.seg.w+(2*self.margin) + self.seg.h+self.margin, 3*self.margin+self.seg.w+self.seg.h, False], 
        [self.seg.w+(2*self.margin), self.seg.h+self.margin*6+self.seg.w, True], 
        [self.margin, 3*self.margin+self.seg.w+self.seg.h, False],
        [self.margin, 2*self.margin+self.seg.w, False],
        [self.seg.w +2*self.margin, self.seg.h+self.seg.w+2*self.margin, True]]
        
    def update(self):
        for i in self.pos:
            s = Segment(i[0]+self.x, i[1], i[2], (int(self.number)>>self.pos.index(i))& 1)
            s.show()

            
    
