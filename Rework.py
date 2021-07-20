import robot
r = robot.RobotController()
r.connect()

def checkIssue():
    if r.scan_for_people() == True:
        r.rescue_person()
    if r.scan_for_fire() == True:
        while r.scan_for_fire() == True:
            r.extinguish_fire()

def roomOne():
    r.forward(366.7) 
    r.rotate_counterclockwise(85) 

def markerValue(): #If the marker reads a 1 we should do something. If it reads a 2 we skip
    if r.read_marker() == 1:
        return

roomOne()