img = loadImage("Point.png")

def setup():
    global a
    a = 0
    size(600,600)
    background(255)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(100)
    translate(width/2, height/2)
    text("You're Cancelled", 0,0)

def draw():
    colorText()

def colorText():
    global a
    fill(random(0,255),random(0,255),0)
