from sys import argv
from os.path import exists
from random import randint
import os
import time

uniqID = 1000
#rm_el_frogarena See for generating waves of enemies

def generateFloors(out_file):
    floorSpr = ["spr_N_FloorPatchBig","spr_W_FloorPatchBBig","spr_W_FloorPatchBSmall"]
    scenerySpr = floorSpr
    sceneryID = 12+31
    for i in range(0, 15*2):
        sceneryID += 1
        sprIndex = randint(0,len(scenerySpr)-1)
        sceneryX = randint(0,2000)
        sceneryY = randint(0,2000)
        out_file.write("\n     obj,Scenery,"+`sceneryID`+","+`sceneryX`+","+`sceneryY`+",9,-999999,++,0="+scenerySpr[sprIndex]+",1=1,2=0,3=0,k=0,p=-4,fp=0,4=0,5=0,f=1,l=0,")
        
def spawnLoot(out_file,xPos,yPos):
    global uniqID
    lootValue = randint(0,10)
    if lootValue <= 3: #Healthkit
        uniqID += 1
        out_file.write("\n     obj,HealthKit,"+`uniqID`+","+`xPos`+","+`yPos`+",3,-999999,++,")
    elif lootValue <= 5: #Gearbit
        uniqID += 1
        out_file.write("\n     obj,Spawner,"+`uniqID`+","+`xPos-15`+","+`yPos-15`+",4,-999999,++,-1=GearbitCrate,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,")
        uniqID += 1
        out_file.write("\n     obj,Spawner,"+`uniqID`+","+`xPos-15`+","+`yPos+15`+",4,-999999,++,-1=GearbitCrate,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,")
        uniqID += 1
        out_file.write("\n     obj,Spawner,"+`uniqID`+","+`xPos+15`+","+`yPos-15`+",4,-999999,++,-1=GearbitCrate,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,")
        uniqID += 1
        out_file.write("\n     obj,Spawner,"+`uniqID`+","+`xPos+15`+","+`yPos+15`+",4,-999999,++,-1=GearbitCrate,-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,")
    elif lootValue <= 8: #Outfit
        uniqID += 1
        outfitType = randint(0,2)
        outfitLootVal = randint(1,10)
        outfitSpriteVal = outfitLootVal + 1
        
        if outfitType == 1:
            out_file.write("\n     obj,DrifterBones_Outfit,"+`uniqID`+","+`xPos`+","+`yPos`+",3,-999999,++,spr=spr_UiSwordIcon,i="+`outfitLootVal`+",f=0,k=0,g=0,c=0,s="+`outfitSpriteVal`+",w=-999999,")
        elif outfitType == 2:                    
            out_file.write("\n     obj,DrifterBones_Outfit,"+`uniqID`+","+`xPos`+","+`yPos`+",3,-999999,++,spr=spr_uiCapeIcon,i="+`outfitLootVal`+",f=0,k=0,g=0,c="+`outfitSpriteVal`+",s=0,w=-999999,")
        else:
            out_file.write("\n     obj,DrifterBones_Outfit,"+`uniqID`+","+`xPos`+","+`yPos`+",3,-999999,++,spr=spr_ghost,i="+`outfitLootVal`+",f=0,k=0,g="+`outfitSpriteVal`+",c=0,s=0,w=-999999,")
    else:
        uniqID += 1
        weaponType = randint(1,5)
        if weaponType == -1: #The pistol cannot be picked up if other weapons are picked up
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=1,f=0,k=0,g=0,c=0,s=0,w=1,")
        elif weaponType == 2:
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=2,f=0,k=0,g=0,c=0,s=0,w=2,")
        elif weaponType == 3:
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=21,f=0,k=0,g=0,c=0,s=0,w=21,")
        elif weaponType == 4:
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=23,f=0,k=0,g=0,c=0,s=0,w=23,")
        elif weaponType == 5:
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=41,f=0,k=0,g=0,c=0,s=0,w=41,")
        else:
            out_file.write("\n     obj,DrifterBones_Weapon,"+`uniqID`+","+`xPos`+","+`yPos`+",8,-999999,++,spr=spr_itemsGUI,i=43,f=0,k=0,g=0,c=0,s=0,w=43,")

def spawnMobs(out_file,mobName,xStart,xEnd,yStart,yEnd,count):
    global uniqID
    for i in range(0, count):
        uniqID += 1
        mobX = randint(xStart,xEnd)
        mobY = randint(yStart,yEnd)
        out_file.write("\n     obj,Spawner,"+`uniqID`+","+`mobX`+","+`mobY`+",4,-999999,++,-1="+mobName+",-2=-999999,-4=1,-5=0,-6=-1,-7=0,-8=0,")
        
def spawnScenery(out_file,sceneryName,xStart,xEnd,yStart,yEnd,count):
    sceneryID = 12+31+10
    for i in range(0, count):
        sceneryID += 1
        sceneryX = randint(xStart,xEnd)
        sceneryY = randint(yStart,yEnd)
        out_file.write("\n     obj,Scenery,"+`sceneryID`+","+`sceneryX`+","+`sceneryY`+",2,-999999,++,0="+sceneryName+",1=0,2=0,3=0,k=0,p=-4,fp=0,4=0,5=0,f=0,l=0,")
    
def generateLevelContent(out_file,cols,rows,difficulty):
    scenerySpr = ["spr_WTree03Massive","spr_WTree03Massive","spr_WTree03Massive","spr_G_UberBlock_M","spr_NRockBlock16","spr_NRockBlock16","spr_NRockBlock48","spr_NRockBlock48","spr_WTree02Lg","spr_WTree02Lg","spr_WTree02Lg","spr_WTree02Lg","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_WTree01Sm","spr_G_UberBlock_S","spr_G_UberBlock_S","spr_G_UberBlock_L","spr_WTree00General","spr_WStump","spr_WTree02Fallen","spr_WStatueTanuki","spr_WStatueTanuki_side","spr_W_WarriorsRest","spr_W_Tent_01"]
    densityObj = [1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]
    
    mobEasyName = ["slime","SmallCrystalSpider","Grumpshroom","dirk","TanukiSword"] #"Wolf",
    mobEasyDensity = [2,2,2,2,1] #2, (removed Wolves)
    mobEasySet = [mobEasyName,mobEasyDensity]
    mobMediumName = ["RifleDirk","missiledirk","NinjaStarFrog","CultBird","TanukiGun","SpiralBombFrog","BlaDirk"]
    mobMediumDensity = [2,1,2,2,2,2,2]
    mobMediumSet = [mobMediumName,mobMediumDensity]
    mobHardName = ["Leaper","GhostBeamBird","CrystalBaby","Dirkommander","Melty"]
    mobHardDensity = [1,1,1,1,1]
    mobHardSet = [mobHardName,mobHardDensity]
    mobSets = [mobEasySet,mobMediumSet,mobHardSet]
    
    xStart = 150
    xEnd = 2000
    yStart = 60
    yEnd = 2000
    xInc = (xEnd - xStart)/cols
    yInc = (yEnd - yStart)/rows
    
    for c in range (1,cols+1):
        xSpawnStart = xStart + xInc*(c-1)
        xSpawnEnd = xStart + xInc*(c)
        for r in range (1,rows+1):
            ySpawnStart = yStart + yInc*(r-1)
            ySpawnEnd = yStart + yInc*(r)
            spawnValue = randint(1,100)
            if c <= 2 or spawnValue <= 100-difficulty*7:
                sceneIdx = randint(0,len(scenerySpr)-1)
                spawnScenery(out_file,scenerySpr[sceneIdx],xSpawnStart,xSpawnEnd,ySpawnStart,ySpawnEnd,densityObj[sceneIdx])
            elif spawnValue <= 100-difficulty*6:
                print("$$$$---LOOT----$$$$")
                spawnLoot(out_file,(xSpawnStart+xSpawnEnd)/2,(ySpawnStart+ySpawnEnd)/2)
            else:
                scaleType = getDifficultyScale(difficulty)-1
                scaleDensity = getDifficultyScale(difficulty)
                mobSet = mobSets[scaleType]
                mobIndex = randint(0,len(mobSet[0])-1)
                mobName = mobSet[0][mobIndex]
                mobNumber = scaleDensity * mobSet[1][mobIndex]
                print("Spawning "+`mobNumber`+" "+mobName)
                spawnMobs(out_file,mobName,xSpawnStart,xSpawnEnd,ySpawnStart,ySpawnEnd,mobNumber)

def getDifficultyScale(difficulty):
    scale = 1
    randNum = randint(1,10+difficulty)
    if randNum <= 9:
        scale = 1
    elif randNum <= 11:
        scale = 2
    else: 
        scale = 3
    return scale
        
startDifficulty = 3
generation = (startDifficulty)*5
lastRead = 0
lastTime = 0.0

target = open("mapgenTemplate.txt")
target_data = target.read()
target.close()

while 1 < 2:
    if time.time()-lastTime > 2.0:
        lastTime = time.time()
        currRead = os.stat('central/rm_c_backertabletx.lvl').st_atime
        if lastRead != currRead:
            lastRead = currRead
            generation += 1
            difficulty = generation/5
            if difficulty > 10:
                difficulty = 10
            print "///HLD Level Generator///--------------"
            print "Difficulty: "+`difficulty`

            print "   Opening Template..."


            out_file = open('west/rm_wc_minilab.lvl', 'w')
            out_file.truncate()
            out_file.write(target_data)
            print "   Generating Floors..."
            generateFloors(out_file)
            print "   Generating Content"
            generateLevelContent(out_file,5*5,3*5-1,difficulty)
            print "\n\n"
            out_file.close()
