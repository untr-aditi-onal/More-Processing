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
    fill(0)
    background (255,199,0)
    text("movement, not moment",
         random(0,width), random(0,height))

    #moveText()

#def moveText():
    #global a 
    #translate (width/2, height/2)
