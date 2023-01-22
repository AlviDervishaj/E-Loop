from random import randrange
from sprites import score, bomb_group
from helpers import Bomb
from constants import SCREEN_WIDTH

waveIndex: int = 1
wave_step: int = 1
spawnCount: int = 0
bombLastSpawnTime: int = 0
bombsDefaultRisingTime: int = 1500
bombsDefaultPeakTime: int = 1200
bombsDefaultDropTime: int = 2000
waitTime: int = 1500

def wave_handler() -> None:
    global waveIndex
    if(waveIndex%10 == 0):
        # THis is the space to implement the manual/special waves
        pass
    elif(waveIndex%5 == 0):
        # This will be another wave we will implement / maybe a break wave ?
        pass
    else:
        wave_generator(waveIndex)
        #waveIndex += 1

def wave_generator(waveIndex: int) -> None:
    global wave_step
    if(wave_step == 1):
        Rising(waveIndex)
    elif(wave_step == 2):
        Peak(waveIndex)
    elif(wave_step == 3):
        Rising(waveIndex)
    elif(wave_step == 4):
        Drop()
    # always space for more wavestepId we can implement subwaves inside waves


def Rising(waveIndex: int) -> None:
    global wave_step, spawnCount, bombLastSpawnTime, bombsDefaultRisingTime
    waveSpawnCount = (waveIndex-1) * 20 + 20
    if(spawnCount < waveSpawnCount):
        flip = randrange(0,2)
        x = 1
        if(flip == 1):
            x = -1

        PatternSelector_Rising(x, bombsDefaultRisingTime, waveIndex)

    if(spawnCount == waveSpawnCount):
        wave_step += 1
        spawnCount = 0

def Peak(waveIndex: int) -> None:
    global wave_step, spawnCount, bombLastSpawnTime, bombsDefaultPeakTime
    waveSpawnCount = (waveIndex-1) * 30 + 40
    if(spawnCount < waveSpawnCount):
        flip = randrange(0,2)
        x = 1
        if(flip == 1):
            x = -1
        
        PatternSelector_Peak(x, bombsDefaultPeakTime, waveIndex)

    if(spawnCount == waveSpawnCount):
        wave_step = 3
        spawnCount = 0

def Drop() -> None:
    global waveIndex, wave_step, spawnCount, bombLastSpawnTime, bombsDefaultDropTime
    waveSpawnCount = (waveIndex-1) * 15 + 15
    if(spawnCount < waveSpawnCount):
        flip = randrange(0,2)
        x = 1
        if(flip == 1):
            x = -1
        
        PatternSelector_Drop(x, bombsDefaultDropTime, waveIndex)

    if(spawnCount == waveSpawnCount):
        wave_step = 1
        waveIndex += 1
        spawnCount = 0

def Group(spawnCount: int, isFliped: int, skipChance: int, chanceDecreasingRate: int, waveIndex) -> None:
    spawnPositionX = randrange(40, SCREEN_WIDTH-39, 80)
    skipChanceConstraint = 0
    # we use this loop to simultaniously spawn set number of bombs (5)
    for i in range(spawnCount):
        skipOne = randrange(0,10)
        if(skipOne >= skipChance - skipChanceConstraint):
            spawnPosition = ((spawnPositionX + (isFliped*i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)
        else:
            skipChanceConstraint += chanceDecreasingRate

def Ladder(spawnCount: int, isFliped: int, skipChance: int, chanceDecreasingRate: int, waveIndex) -> None:
    spawnPositionX = randrange(40, SCREEN_WIDTH-39, 80)
    skipChanceConstraint = 0
    # we use this loop to simultaniously spawn set number of bombs (5)
    for i in range(spawnCount):
        skipOne = randrange(0,10)
        if(skipOne >= skipChance - skipChanceConstraint):
            spawnPosition = ((spawnPositionX + (isFliped*i)*80), -(1000+i*30))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)
        else:
            skipChanceConstraint += chanceDecreasingRate

def Row(skipTwo: bool, waveIndex) -> None:
    spawnPositionX = 40
    skipOne = randrange(0,16)
    skip = -1
    if(skipTwo):
        skip = skipOne + 1
    for i in range(16):
        if(i != skipOne and i != skip):
            spawnPosition = ((spawnPositionX + (i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)

def Middle(skipOne: bool, waveIndex) -> None:
    spawnPositionX = 40
    skip = 0
    if(skipOne):
        skip = randrange(5,11)
    for i in range(16):
        if(i >= 5 and i < 11 and i != skip):
            spawnPosition = ((spawnPositionX + (i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)

def  Corner(lessBombs: int, waveIndex) -> None:
    spawnPositionX = 40
    for i in range(16):
        if(i < (5 - lessBombs) or i >= (11 + lessBombs)):
            spawnPosition = ((spawnPositionX + (i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)

def Left(lessBombs: int, waveIndex) -> None:
    spawnPositionX = 40
    skipOne = randrange(0,(8 - lessBombs))
    for i in range(16):
        if(i < (8 - lessBombs) and i != skipOne):
            spawnPosition = ((spawnPositionX + (i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)

def Right(lessBombs: int, waveIndex) -> None:
    spawnPositionX = 40
    skipOne = randrange((8 + lessBombs),16)
    for i in range(16):
        if(i >= (8 + lessBombs) and i != skipOne):
            spawnPosition = ((spawnPositionX + (i)*80), -(1000))
            new_bomb = Bomb(spawnPosition, waveIndex)
            bomb_group.add(new_bomb)

def PatternSelector_Peak(isFliped: int, defaultWaitTime: int, waveIndex) -> None:
    randomPattern = randrange(0,200)
    global bombLastSpawnTime, spawnCount, waitTime
    if(score.scoretimer - bombLastSpawnTime > waitTime):
        if(randomPattern < 25):
            Group(5,isFliped,4,2, waveIndex)
            waitTime = defaultWaitTime
        elif(randomPattern < 50):
            Ladder(8, isFliped, 2, 2, waveIndex)
            waitTime = defaultWaitTime + 1000
        elif(randomPattern < 75):
            Row(False, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 100):
            Middle(False, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 125):
            Corner(0, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 150):
            Left(0, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 175):
            Right(0, waveIndex)
            waitTime = defaultWaitTime + 400
        else:
            Group(2,isFliped,0,0, waveIndex)
            waitTime = defaultWaitTime
        spawnCount += 1
        bombLastSpawnTime = score.scoretimer

def PatternSelector_Rising(isFliped: int, defaultWaitTime: int, waveIndex) -> None:
    randomPattern = randrange(0,400)
    global bombLastSpawnTime, spawnCount, waitTime
    if(score.scoretimer - bombLastSpawnTime > waitTime):
        if(randomPattern < 100):
            Group(5,isFliped,4,2, waveIndex)
            waitTime = defaultWaitTime
        elif(randomPattern < 130):
            Ladder(7, isFliped, 3, 2, waveIndex)
            waitTime = defaultWaitTime + 1000
        elif(randomPattern < 160):
            Row(True, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 195):
            Middle(True, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 230):
            Corner(2, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 265):
            Left(2, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 300):
            Right(2, waveIndex)
            waitTime = defaultWaitTime + 400
        else:
            Group(2,isFliped,0,0, waveIndex)
            waitTime = defaultWaitTime
        spawnCount += 1
        bombLastSpawnTime = score.scoretimer

def PatternSelector_Drop(isFliped: int, defaultWaitTime: int, waveIndex) -> None:
    randomPattern = randrange(0,200)
    global bombLastSpawnTime, spawnCount, waitTime
    if(score.scoretimer - bombLastSpawnTime > waitTime):
        if(randomPattern < 50):
            Group(5,isFliped,4,2, waveIndex)
            waitTime = defaultWaitTime
        elif(randomPattern < 80):
            Ladder(6, isFliped, 2, 2, waveIndex)
            waitTime = defaultWaitTime + 1000
        elif(randomPattern < 95):
            Row(True, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 120):
            Middle(True, waveIndex)
            waitTime = defaultWaitTime + 400
        elif(randomPattern < 150):
            Corner(3, waveIndex)
            waitTime = defaultWaitTime + 400
        else:
            Group(2,isFliped,0,0, waveIndex)
            waitTime = defaultWaitTime
        spawnCount += 1
        bombLastSpawnTime = score.scoretimer