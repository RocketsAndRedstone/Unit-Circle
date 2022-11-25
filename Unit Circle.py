import turtle

def main():
  TURTLE = turtle.Turtle()
  TURTLE.hideturtle()
  TURTLE.speed(0)
  radius = 194
  listOfPoints = list()
  showLines(TURTLE , radius)
  print(listOfPoints)
  setPoints(TURTLE , radius , listOfPoints)
  print(listOfPoints)
  putstamps(TURTLE , listOfPoints)
  putText(TURTLE , listOfPoints)
  
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

def setPoints(TURTLE , radius , listOfPoints):
    TURTLE.penup()
    index = 0
    rotation = 0
    rotation1 = 30
    rotation2 = 15
    
    def getpoint(TURTLE , listOfPoints , rotation , index , radius):
        TURTLE.home()
        TURTLE.lt(rotation)
        TURTLE.forward(radius)
        point = TURTLE.position()
        listOfPoints.insert(index , point)
        return listOfPoints
        
    while rotation < 350:
        getpoint(TURTLE , listOfPoints , rotation , index , radius)
        index += 1
        rotation += rotation1
        getpoint(TURTLE , listOfPoints , rotation , index , radius)
        index += 1
        rotation += rotation2
        getpoint(TURTLE , listOfPoints , rotation , index , radius)
        index += 1
        rotation += rotation2
        getpoint(TURTLE , listOfPoints , rotation , index , radius)
        index += 1
        rotation += rotation1

    return listOfPoints

def putstamps(TURTLE , listOfPoints):
    counter = 0
    TURTLE.color("blue")
    while counter <= 14: 
        TURTLE.penup()
        TURTLE.setposition(listOfPoints[counter])
        TURTLE.stamp()
        counter += 1
    TURTLE.color("black")
    TURTLE.penup()
    TURTLE.home()
def putText(TURTLE , listOfPoints):
    point = 0
    text = 0
    while point <= 15:
        TURTLE.setposition(listOfPoints[point])
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
