## A program that creates a Unit Circle with the coordinates of each point marked with a blue stamp and labeled with the coordinates in red. The angle measurements in degrees and radians are written next to the coordinates in dark green.
## The color of each item can be changed though there is no central variable to do so. The size of the circle itself can be modified by changing the radius variable in the main function. There may be options to further optimize this
## program but due to time restraints, this is the best that could be done.
import turtle

def main():
  ##Creates the main variables and list that will be used Throughout the program as well as calling each function in turn.
  TURTLE = turtle.Turtle()
  TURTLE.hideturtle()
  TURTLE.speed(0)
  radius = 174
  listOfPoints = list()
  setPoints(TURTLE , radius , listOfPoints)
  TURTLE.speed(8)
  simplelines(TURTLE , listOfPoints , radius)
  putstamps(TURTLE , listOfPoints)
  TextToShow(TURTLE , listOfPoints)

def outerCircle(TURTLE , radius):
  ## draws the outer circle using the radius in the main function
  TURTLE.penup()
  TURTLE.setposition(0 , (-radius))
  TURTLE.pendown()
  TURTLE.circle(radius)
  TURTLE.penup()

def setPoints(TURTLE , radius , listOfPoints):
    ## Creates a list of points on the outer circle where each inner radius intersects the outer circle
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

def simplelines(TURTLE , listOfPoints , radius):
  ## draws the inner lines of the Unit Circle by "teleporting" the turtle to each point on the outer circle as defined by the list listOfPoints.
  TURTLE.home()
  outerCircle(TURTLE , radius)
  TURTLE.home()
  TURTLE.penup()
  index1 = 0
  index2 = 8
  for i in range(8):
    TURTLE.setposition(listOfPoints[index1])
    TURTLE.pendown()
    TURTLE.setposition(listOfPoints[index2])
    TURTLE.penup()
    index1 += 1
    index2 += 1
    
def putstamps(TURTLE , listOfPoints):
  ## puts a stamp on the outer circle to indicate where information will be displayed
    counter = 0
    TURTLE.color("blue")
    TURTLE.home()
    while counter <= 15: 
        TURTLE.penup()
        TURTLE.setposition(listOfPoints[counter])
        TURTLE.stamp()
        counter += 1
    TURTLE.color("black")
    TURTLE.penup()
    TURTLE.home()
    
def pointZeroinfo(TURTLE , listOfPoints):
  ## Write the information out for the zero degree radius. Called point zero due to the index of this point in listOfPoints.
  TURTLE.setposition(listOfPoints[0])
  toBeDisplayed = "(1 , 0)"
  x = len(toBeDisplayed)
  y = ""
  ## used to change the color of the text between the coordinates and the angle measurements, used in the next fifteen or so functions, though for the functions that write out the information for angles between 120 and 270,
  ## there is a different approach
  for i in range(x + 2):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + "  0°  , 0 radians")
  TURTLE.color("red")

def pointOneInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[1])
  toBeDisplayed = "(√3/2 , 1/2)"
  x = len(toBeDisplayed)
  y = ""
  for i in range(x + 6):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 30° , π/6 radians")
  TURTLE.color("red")

def pointTwoInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[2])
  toBeDisplayed = "(√2/2 , √2/2)"
  TURTLE.write(toBeDisplayed)
  x = len(toBeDisplayed)
  y = ""
  for i in range(x + 7):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 45° , π/4 radians")
  TURTLE.color("red")
  
def pointThreeInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[3])
  toBeDisplayed = "(1/2 , √3/2)"
  TURTLE.write(toBeDisplayed)
  x = len(toBeDisplayed)
  y = ""
  for i in range(x + 6):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 60° , π/3 radians")
  TURTLE.color("red")
 
def pointFourInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[4])
  toBeDisplayed = "(0 , 1)"
  TURTLE.write(toBeDisplayed)
  x = len(toBeDisplayed)
  y = ""
  for i in range(x + 3):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 90° , π/2 radians")
  TURTLE.color("red")
  
def pointFiveInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[5])
  toBeDisplayed = "(-1/2 , √3/2)"
  y = "  120° , 2π/3 radians"
  x = len(toBeDisplayed + y)
  x *= 4.55
  TURTLE.lt(180)
  TURTLE.forward(x)
  ## the use of this different approach is to ensure that the differentiating colors of the chordates and angle measurements stays consistent
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 2.6
  TURTLE.forward(-x)
  TURTLE.write(y)
  TURTLE.color("red")
 
def pointSixInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[6])
  toBeDisplayed = "(-√2/2 , √2/2)"
  y = "  135° , 3π/4 radians"
  x = len(toBeDisplayed + y)
  x *= -4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 3
  TURTLE.forward(x)
  TURTLE.write(y)
  TURTLE.color("red")

def pointSevenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[7])
  toBeDisplayed = "(-√3/2 , 1/2)"
  y = "  150° , 5π/6 radians"
  x = len(toBeDisplayed + y)
  x *= 4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 2.6
  TURTLE.forward(-x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointEightInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[8])
  toBeDisplayed = "(-1 , 0)"
  x = len(toBeDisplayed)
  y = "  180° , π radians"
  x = len(toBeDisplayed + y)
  x *= -4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 1.6
  TURTLE.forward(x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointNineInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[9])
  toBeDisplayed = "(-√3/2 , -1/2)"
  x = len(toBeDisplayed)
  y = "  210° , 7π/6 radians"
  x = len(toBeDisplayed + y)
  x *= 4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 2.9
  TURTLE.forward(-x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointTenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[10])
  toBeDisplayed = "(-√2/2 , -√2/2)"
  x = len(toBeDisplayed)
  y = "  225° , 5π/4 radians"
  x = len(toBeDisplayed + y)
  x *= -4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 3.2
  TURTLE.forward(x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointElevenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[11])
  toBeDisplayed = "(-1/2 , -√3/2)"
  x = len(toBeDisplayed)
  y = "  240° , 4π/3 radians"
  x = len(toBeDisplayed + y)
  x *= 4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 2.9
  TURTLE.forward(-x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointTwelveInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[12])
  toBeDisplayed = "(0 , -1)"
  x = len(toBeDisplayed)
  y = "  270° , 3π/2 radians"
  x = len(toBeDisplayed + y)
  x *= -4.58
  TURTLE.lt(180)
  TURTLE.forward(x)
  TURTLE.write(toBeDisplayed)
  toBeDisplayed.rstrip(y)
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  x = len(y)
  x *= 1.5
  TURTLE.forward(x)
  TURTLE.write(y)
  TURTLE.color("red")
  
def pointThirteenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[13])
  toBeDisplayed = "   (1/2 , -√3/2)"
  x = len(toBeDisplayed)
  TURTLE.write(toBeDisplayed)
  y = ""
  for i in range(x + 6):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 300° , 5π/3 radians")
  TURTLE.color("red")
  
def pointFourteenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[14])
  toBeDisplayed = "  (√2/2 , -√2/2)"
  x = len(toBeDisplayed)
  TURTLE.write(toBeDisplayed)
  y = ""
  for i in range(x + 8):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 315° , 7π/4 radians")
  TURTLE.color("red")
  
def pointFifteenInfo(TURTLE , listOfPoints):
  TURTLE.setposition(listOfPoints[15])
  toBeDisplayed = " (√3/2 , -1/2)"
  x = len(toBeDisplayed)
  TURTLE.write(toBeDisplayed)
  y = ""
  for i in range(x + 6):
    y += " "
  TURTLE.write(toBeDisplayed)
  TURTLE.color("dark green")
  TURTLE.write(y + " 330° , 11π/6 radians")
  
def TextToShow(TURTLE , listOfPoints):
  ## calls all the functions that write out information onto the screen
  TURTLE.color("red")
  pointZeroinfo(TURTLE , listOfPoints)
  pointOneInfo(TURTLE , listOfPoints)
  pointTwoInfo(TURTLE , listOfPoints)
  pointThreeInfo(TURTLE , listOfPoints)
  pointFourInfo(TURTLE , listOfPoints)
  pointFiveInfo(TURTLE , listOfPoints)
  pointSixInfo(TURTLE , listOfPoints)
  pointSevenInfo(TURTLE , listOfPoints)
  pointEightInfo(TURTLE , listOfPoints)
  pointNineInfo(TURTLE , listOfPoints)
  pointTenInfo(TURTLE , listOfPoints)
  pointElevenInfo(TURTLE , listOfPoints)
  pointTwelveInfo(TURTLE , listOfPoints)
  pointThirteenInfo(TURTLE , listOfPoints)
  pointFourteenInfo(TURTLE , listOfPoints)
  pointFifteenInfo(TURTLE , listOfPoints)
  TURTLE.color("black")
  TURTLE.home()

main()
