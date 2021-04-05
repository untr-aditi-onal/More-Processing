add_library('sound')

def setup():
    global pulse
    size(600,600)
    background(255,0,0)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(0,0,255)
    translate(width/2, height/2)
    text("I wish we weren't so polarized", 0,0)
    pulse = Pulse(this)
    pulse.amp(0.5)

def draw():
    global pulse
    pulse.freq(mouseX)
    pulse.play()
    #(Sgn( sin theta) + 1) * amplitude
