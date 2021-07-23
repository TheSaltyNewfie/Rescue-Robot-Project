import robot
import math
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

r = robot.RobotController()
r.connect()

tempList = []

def markerValue(): #If the marker reads a 1 we should do something. If it reads a 2 we skip
    if r.read_marker() == 1:
        return True
    if r.read_marker() == 2:
        return False

def roomOne(): #Room 1, checks for fire and people
    if markerValue() == True:
        r.left(650)
        tempList.append(r.take_temperature())
        if r.scan_for_people() == True:
            r.rescue_person()
            r.right(670)
            r.forward(-300)
            r.forward(300)
        elif r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.right(670)
        else:
            r.right(670)
    if markerValue() == False:
        pass

def roomTwo(): #Room 2, checks for fire and people
    if markerValue() == True:
        r.left(650)
        r.forward(85)
        tempList.append(r.take_temperature())
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
            r.forward(-85)
            r.right(650)
    if markerValue() == False:
        pass

def roomThree(): #Room 3, checks for fire and people
    if markerValue() == True:
        r.rotate_counterclockwise(90)
        r.forward(300)
        tempList.append(r.take_temperature())
        r.forward(-300)#! Leave this here, it tells the bot how to leave
        r.rotate_clockwise(90)#! Leave this here, it tells the bot how to leave
    if markerValue() == False:
        pass

def roomFour(): #Room 4, checks for fire and people
    if markerValue() == True:
        r.forward(445)
        r.left(500)
        r.rotate_counterclockwise(90)
        tempList.append(r.take_temperature())
        if r.scan_for_people() == True:
            r.rescue_person()
            r.forward(-500)
            r.right(-440)
        elif r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.forward(-500)
            r.right(-440)
        else:
            r.forward(-500)
            r.right(-440)
    if markerValue() == False:
        r.rotate_counterclockwise(90)
        

def roomFive():
    if markerValue() == True:
        r.right(300)
        r.forward(250)
        tempList.append(r.take_temperature())
        if r.scan_for_people() == True:
            r.rescue_person()
            r.forward(-285)
            r.right(-350)
        elif r.scan_for_fire() == True:
            while r.scan_for_fire() == True:
                r.extinguish_fire()
            r.forward(-285)
            r.right(-350)
        else:
            r.forward(-285)
            r.right(-350)
        
    if markerValue() == False:
        pass

def tempMath(): 
    average = sum(tempList) / len(tempList)
    return average

def tempGraph():
    xs = []
    for num in range(0, len(tempList)):
        xs.append(num)
    
    plt.plot(xs, tempList)
    plt.show()


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
r.left(690)
r.forward(865)
print(f'This room ID is: {r.read_marker()}')
roomFour()
r.forward(1450)
r.right(200)
print(f'This room ID is: {r.read_marker()}')
roomFive()
r.left(150)
r.forward(-1430)
r.left(850)
r.forward(-750)
r.left(900)
r.forward(2250)
r.right(1490)
print(f'The temperature for each room is as follows: {tempList} \nAverage Temp = {tempMath()}')
tempGraph()