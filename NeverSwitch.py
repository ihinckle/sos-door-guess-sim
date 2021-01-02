'''
will never switch door
'''
from random import randint

doors = [1, 2, 3]

prizeDoor = None
pickedDoor = None
unusedDoors = []
gamesPlayed = 0;
gamesWon = 0;

def init():
    global doors
    global unusedDoors
    doors = [1, 2, 3]
    unusedDoors = []

def definePrizeDoor():
    return randint(1, 3)

def pickDoor():
    return randint(1, 3)

def remainingDoors(prize, picked):
    doors = []
    for i in range(1, 4):
        if(i != prize and i != picked):
            doors.append(i)
    return doors

def removeDoor(prize, picked):
    prizeIndex = doors.index(prize)
    pickedIndex = doors.index(picked)
    randomIndex = None;
    if prize != picked:
        del doors[3-prizeIndex-pickedIndex]
    if prize == picked:
        while randomIndex is None or randomIndex == prizeIndex:
            randomIndex = randint(0, 2)
        del doors[randomIndex]
        
def checkWin(prize, picked):
    global gamesWon
    if prize == picked:
        gamesWon += 1
#         print('you won')
#     else:
#         print('you lost')
    

def playGame():
    global gamesPlayed
    gamesPlayed += 1
    prizeDoor = definePrizeDoor()
#     print('prize door is: '+prizeDoor.__str__())
    pickedDoor = pickDoor()
#     print('picked door is: '+pickedDoor.__str__())
    unusedDoors = remainingDoors(prizeDoor, pickedDoor)
#     print('unused doors are: '+unusedDoors.__str__())
    removeDoor(pickedDoor, prizeDoor)
#     print('remaining doors are: '+doors.__str__())
    checkWin(pickedDoor, prizeDoor)
    
while gamesPlayed < 1000000:
    init()
    playGame()
    
print('win percentage: '+(gamesWon/gamesPlayed).__str__())