from Segment import Segment
from SevenSegments import SevenSegments

segs = SevenSegments(" ",0)
word = list("frolloccone")
print(word)
errors = ["K", "M", "Q", "R", "T", "V", "W", "X", "Y", "Z"]
def setup(): 
  background(0)
  noStroke()
  fill(102)
  size(segs.SegmentW * len(word), segs.SegmentH)
  for c in range(len(word)):
      if c in errors :
        pass
      else:
        s = SevenSegments(word[c], segs.SegmentW * c)
        s.update()
      

def KeyTyped():
    if keyCode==ENTER:
        for c in range(len(word)):
            s = SevenSegments(word[c], segs.SegmentW * c)
            s.update()
        print(word)
    
    else:
        word.append(str(keycode))
        
