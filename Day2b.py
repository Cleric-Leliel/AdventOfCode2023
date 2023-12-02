#Advent of Code 2023
#Day 2: Cube Color Game
#part 2:  reverse cube question
#v1.0  12-02-2023

import re

with open('Day2in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0

for i in range(0,len(read_data)):
        prod =0
        game =read_data[i].strip().split(": ")     #pull out the game number
        gameID = game.pop(0)
        gameID = gameID.replace("Game ","")
        colorsums = {"red": 0, "blue":0, "green":0}
        game = re.split(', |; | ', game[0])

        for x in range(1,len(game)):
            color = game[x]
            if color in colorsums.keys() and (int(game[x-1]) > colorsums[color]):   #keep only highest seen num per color
                colorsums.update ({color : int(game[x-1])})
            elif not (color in colorsums.keys()) and not(color.isdigit()):
                print("ERROR color = ", color, " for ", gameID, " ",game)  #just a lil error checking
                
        prod = colorsums["red"]  * colorsums["blue"] * colorsums["green"]
        sumtot = sumtot + prod

print("sumtot: ",sumtot)
