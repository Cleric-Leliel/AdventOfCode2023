#Advent of Code 2023
#Day 6: Wait For It
#v1.0  12-06-2023

import re
import math

with open('Day6in.txt') as f:
    read_data = f.readlines()
f.close()

times = read_data[0].strip().split(':')   #could redo this to avoid the arrays entirely, but w/e.
del times[0]
times[0] = times[0].replace(" ","")
record = read_data[1].strip().split(':')
del record[0]
record[0] = record[0].replace(" ","")

print(times,record)

t = int(times[0])
maxt = math.ceil((t)/2)
for hold in range (0,maxt):
        dist = (int(t) - hold)*hold
        #print(" hold for ",hold,"for dist",dist)
        if dist > int(record[0]):
            wins = 2*(maxt-hold)               
            if (t % 2) == 0:   # there is a better way to do this
                wins = wins+1
            print(wins, " wins ")
            #prodtot = prodtot * wins
            break

#print("prodtot: ",prodtot)
