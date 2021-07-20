import robot
import PySimpleGUI
import threading


def markerValue(arg1):
    if arg1 == 1:
        print("There is a person")
    if arg1 == 2:
        print("There is a fire")
    if arg1 == 3:
        print("There is nothing")


r = robot.RobotController()
r.connect()

r.forward(400)
r.rotate_counterclockwise(90)
markerValue(r.read_marker())
r.forward(740)
r.rotate_clockwise(90)
r.rescue_person()

