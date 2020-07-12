from Segment import Segment
from SevenSegments import SevenSegments

segs = SevenSegments(" ",0)
word = list("test")
def setup(): 
  background(0)
  noStroke()
  fill(102)
  size(segs.SegmentW * len(word), segs.SegmentH)
  for i in range(len(word)):
    try:
      s = SevenSegments(word[i], segs.SegmentW * i)
      s.update()
    except TypeError:
      
      print("This character can not be written with Seven Segement Displays: {}".format(word[i]))
