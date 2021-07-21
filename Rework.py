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
            r.forward(300)
            print("Finished RoomOne")
        elif r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.right(670)
        else:
            pass #Remove when you test temp code this is here to not throw errors right now
            #! Please put checking temp here
            r.right(670)

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
            r.forward(-850)
        elif r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.forward(-85)
            r.right(650)
        else:
            pass #Remove when you test temp code this is here to not throw errors right now
            #! Copy from room one
            r.forward(-85)#! Leave this here
            r.right(650)#! Leave this here
        r.forward(-85)
        r.right(650)
    if markerValue() == False:
        pass

def roomThree(): #Room 2, checks for fire and people
    if markerValue() == True:
        r.rotate_counterclockwise(90)
        r.forward(100)
        #Put temperature code here
        r.forward(-100)
        r.rotate_clockwise(90)
    if markerValue() == False:
        pass

def roomFour(): #Room 2, checks for fire and people
    if markerValue() == True:
        pass
        #r.rotate_counterclockwise(90)
        #r.forward(100)
        #Put temperature code here
        #r.forward(-100)
        #r.rotate_clockwise(90)
    if markerValue() == False:
        pass

#These are the movement commands
r.forward(370)
r.left(100)
print(f'This room ID is: {r.read_marker()}')
roomOne()
r.forward(550)
print(f'This room ID is: {r.read_marker()}')
roomTwo()
r.forward(430)
r.left(1580)
r.rotate_counterclockwise(90)
print(f'This room ID is: {r.read_marker()}')
roomThree()
r.forward(600)
r.rotate_counterclockwise(90)
r.forward(800)
r.rotate_counterclockwise(90)
r.forward(690)
r.rotate_clockwise(90)
r.forward(850)
print(f'This room ID is: {r.read_marker()}')
roomFour()