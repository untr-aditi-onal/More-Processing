def setup():
    frameRate(10)
    global a
    a = 0
    size(600,600)
    background(255)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(100)
    translate(width/2, height/2)

def draw():
    global a 
    background (255)
    while a < (360):
        a = a+1
        print(a)
        rotateText(a)
    
def rotateText(a):  
    if a < (360):
    #global a
        a = a+random(0,2)
        background (255)
        rotate(radians(a))
        translate(width/2, height/2)
        text("the revolution will not be ig lived", 0,0)
