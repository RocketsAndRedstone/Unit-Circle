import turtle

def main():
  TURTLE = turtle.Turtle()
  TURTLE.hideturtle()
  TURTLE.speed(0)
  radius = 194
  listofpoints = list()
  showLines(TURTLE , radius)
  setPoints(TURTLE , radius , listofpoints)
  print(listofpoints)
  putstamps(TURTLE , listofpoints)
  putText(TURTLE , listofpoints)
  
def outerCircle(TURTLE , radius):
  TURTLE.penup()
  TURTLE.setposition(0 , (-radius))
  TURTLE.pendown()
  TURTLE.circle(radius)
  TURTLE.penup()
  
def primaryHorazantalLine(TURTLE , radius):
  TURTLE.home()
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def primaryVirticalLine(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(90)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)
  
def mainLineOne(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(30)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def mainLineTwo(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(45)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def mainLineThree(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(60)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)
  
def mainLineFour(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(120)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def mainLineFive(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(135)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def mainLineSix(TURTLE , radius):
  TURTLE.penup()
  TURTLE.home()
  TURTLE.lt(150)
  TURTLE.forward(-1 * radius)
  TURTLE.pendown()
  TURTLE.forward(2 * radius)

def setPoints(TURTLE , radius , listofpoints):
    TURTLE.penup()
    index = 0
    TURTLE.home()
    rotation = 0
    rotation1 = 30
    rotation2 = 15
    for i in range(3):
        getpoint(TURTLE , listofpoints , rotation , index)
        index += 1
        rotatinal += rotation1
        getpoint(TURTLE , listofpoints , rotation , index)
        index += 1
        rotation += rotation2
        getpoint(TURTLE , listofpoints , rotation , index)
        index += 1
        rotation += rotation2
        getpoint(TURTLE , listofpoints , rotation , index)
        index += 1
        rotation += rotation1
    
    def getpoint(TURTLE , listofpoints , rotation , index):
        TURTLE.home()
        TURTLE.lt(rotation)
        TURTLE.forward(radius)
        point = turtle.position()
        listofpoints.insert(index , point)
        return listofpoints
        


    
    
    
def putstamps(TURTLE , listofpoints):
    counter = 0
    TURTLE.color("blue")
    while counter <= 14: 
        TURTLE.penup()
        TURTLE.setposition(listofpoints[counter])
        TURTLE.stamp()
        counter += 1
    TURTLE.color("black")
    TURTLE.penup()
    TURTLE.home()
def putText(TURTLE , listofpoints):
    point = 0
    text = 0
    while point <= 15:
        TURTLE.setposition(listofpoints[point])
        TURTLE.write(f"This is position {text}")
        point += 1
        text += 1

def showLines(TURTLE , radius ):
  outerCircle(TURTLE , radius)
  primaryHorazantalLine(TURTLE , radius)
  primaryVirticalLine(TURTLE , radius)
  mainLineOne(TURTLE , radius)
  mainLineTwo(TURTLE , radius)
  mainLineThree(TURTLE , radius)
  mainLineFour(TURTLE , radius)
  mainLineFive(TURTLE , radius)
  mainLineSix(TURTLE , radius)
  

main()
