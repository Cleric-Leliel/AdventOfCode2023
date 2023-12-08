#Advent of Code 2023
#Day 8: Haunted Wasteland
#v1.0  12-08-2023

import re

with open('Day8in.txt') as f:
    read_data = f.readlines()
f.close()

dmap = {}
totstep = 0
directions = read_data[0].strip()
for i in range(2, len(read_data)):
    line1 = read_data[i].strip().replace(")","")
    line = re.split(' = \(|, ',line1)
    dmap.update({line[0]:[line[1],line[2]]})

j =0
next1 = 'AAA'      #start
while next1 != 'ZZZ' and totstep <=999999:
    last1 = next1
    d = directions[j]
    if d == 'L':
        next1 = dmap[last1][0]
    else:
        next1 = dmap[last1][1]
    j = j+1
    totstep = totstep +1
    if j >=  len(directions):
                j = 0
        

print(totstep)
#print(dmap)


