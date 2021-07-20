import robot
import PySimpleGUI
import threading


def markerValue(arg1):
    if arg1 == 1:
        return 1
    if arg1 == 2:
        return 2
    if arg1 == 3:
        return 3


def roomOne():
    r.forward(366.7) #Pixel perfect for the scanner, position is also float
    r.rotate_counterclockwise(85) # near perfect angle to read the scanner and move into the room
    if r.read_marker() == 1:
        r.forward(700.1) #Pixel perfect for the person in the room
        r.rotate_clockwise(90)
        print(r.rescue_person())
        r.rotate_clockwise(86) # Degrees are not float so best angle here is 86
        r.forward(724)


r = robot.RobotController()
r.connect()

roomOne()


