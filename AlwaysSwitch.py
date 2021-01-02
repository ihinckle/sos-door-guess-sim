'''
will always switch door
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
        
def switchDoor(picked):
    pickedIndex = doors.index(picked)
    return doors[1-pickedIndex]
        
def checkWin(prize, picked):
    global gamesWon
    if prize == picked:
        gamesWon += 1
#         print('you won')
#     else:
#         print('you lost')
    

def playGame():
    global prizeDoor
    global pickedDoor
    global gamesPlayed
    gamesPlayed += 1
    prizeDoor = randint(1, 3)
#     print('prize door is: '+prizeDoor.__str__())
    pickedDoor = randint(1, 3)
#     print('picked door is: '+pickedDoor.__str__())
    removeDoor(pickedDoor, prizeDoor)
#     print('remaining doors are: '+doors.__str__())
    pickedDoor = switchDoor(pickedDoor)
#     print('picked door is: '+pickedDoor.__str__())
    checkWin(pickedDoor, prizeDoor)
    
while gamesPlayed < 1000000:
    init()
    playGame()
    
print('win percentage: '+(gamesWon/gamesPlayed).__str__())