#Advent of Code 2023
#Day 6: Wait For It
#v1.0  12-06-2023

import re
import math

with open('Day6in.txt') as f:
    read_data = f.readlines()
f.close()

prodtot=1

times = read_data[0].strip().split()
del times[0]
record = read_data[1].strip().split()
del record[0]

#Verify: max is always at hold for half
# so run calc until you beat the record
#speed = hold
for tm in range(0,len(times)):
    t = int(times[tm])
    maxt = math.ceil((t)/2)
    #print(tm, " race")
    for hold in range (0,maxt):
        dist = (int(t) - hold)*hold
        #print(" hold for ",hold,"for dist",dist)
        if dist > int(record[tm]):
            wins = 2*(maxt-hold)               #
            if (t % 2) == 0:   # there is a better way to do this
                wins = wins+1
            #print(wins, " wins ")
            prodtot = prodtot * wins
            break

print("prodtot: ",prodtot)
