import robot
r = robot.RobotController()
r.connect()


def markerValue(): #If the marker reads a 1 we should do something. If it reads a 2 we skip
    if r.read_marker() == 1:
        return True
    if r.read_marker() == 2:
        return False

def roomOne(): #Room 1, checks for fire and people
    if markerValue() == True:
        r.left(650)
        if r.scan_for_people() == True:
            r.rescue_person()
            r.right(670)
            r.forward(-300)
        if r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.right(670)
    if markerValue() == False:
        pass

def roomTwo(): #Room 2, checks for fire and people
    if markerValue() == True:
        r.left(650)
        r.forward(85)
        if r.scan_for_people() == True:
            r.rescue_person()
            r.forward(-85)
            r.right(650)
        if r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.forward(-85)
            r.right(650)
    if markerValue() == False:
        pass

#These are the movement commands
r.forward(370)
r.left(100)
roomOne()
r.forward(850)
roomTwo()
