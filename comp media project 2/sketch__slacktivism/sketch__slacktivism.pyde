def setup():
    frameRate(10)
    global a
    a = 0
    size(600,600)
    background(0)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(100)
    translate(width/2, height/2)
    
def draw():
    #background(255)
    fill(255)
    text("#Is this just performative slacktivism?", 
         random(0,width), random(0,height))
