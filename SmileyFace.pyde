x = 100
y = 100
delay = 16

def setup():
    size(400,400)
    background(75)
    
def makeSmileyFace(x,y):
    fill(255,255,0)
    ellipse(x,y,100,100)
    fill(0)
    ellipse(x-20,y-20,10,10)
    ellipse(x+20,y-20,10,10)
    noFill()
    arc(x-20,y,100,25,0,PI/2.0)
    
def draw():
    global x, y
    background(100)
    makeSmileyFace(x,y)
    fc = frameCount

    x += (mouseX-x)/delay
    y += (mouseY-y)/delay
