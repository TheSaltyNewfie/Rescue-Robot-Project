from math import sin
import random
import matplotlib.pyplot as plt

randlist = []
xs = []

def testGraph():
    plt.plot(xs, randlist)
    plt.show()

for i in range(0,5):
    n = random.randint(1,30)
    randlist.append(n)

for num in range(0, len(randlist)):
    xs.append(num)
print(randlist)
print(xs)

def doMath():
    average = sum(randlist) / len(randlist)
    return average



#print(f'List of numbers = {randlist}')
#print(f'Average of these numbers = {doMath()}')
testGraph()
