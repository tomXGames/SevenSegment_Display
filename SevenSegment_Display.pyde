from Segment import Segment
from SevenSegments import SevenSegments

def setup(): 
  size(200, 200)
  background(0)
  noStroke()
  fill(102)
  ss = SevenSegments(1)
  ss.update()
