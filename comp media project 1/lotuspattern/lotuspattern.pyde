def setup():
    size(600,600);
    background(0,0,0);
    fill(219,112,147);

def draw():
    
    if mousePressed:
        drawFlower()
        
def drawFlower():
    translate(mouseX,mouseY)
    rotate(radians(50));
    ellipse(0,0,95,200);
    
    rotate(radians(50));
    ellipse(0,0,95,200);
    
    rotate(radians(50));
    ellipse(0,0,95,200);
    
    rotate(radians(50));
    ellipse(0,0,95,200);
    
    rotate(radians(50));
    ellipse(0,0,95,200);
