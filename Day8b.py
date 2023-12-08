#Advent of Code 2023
#Day 8: Haunted Wasteland
#part 2: Aint Afraid of No Ghosts
#v1.0  12-08-2023

import re
import math

with open('Day8in.txt') as f:
    read_data = f.readlines()
f.close()

dmap = {}
paths ={}   # start [lenpath1, lenpath2]
totstep = 0
directions = read_data[0].strip()
for i in range(2, len(read_data)):
    line1 = read_data[i].strip().replace(")","")
    line = re.split(' = \(|, ',line1)
    dmap.update({line[0]:[line[1],line[2]]})

for pt in dmap:
    j =0
    totstep =0
    if pt[2] == 'A':
        next1 = pt      #start
        while next1[2] != 'Z' and totstep <=999999999:  #may need to increase max totstep
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
        if pt not in paths:
            paths.update({pt:totstep})   #right now only captures first one.  Will LCM work? Prob not since next path could be any length
            

#print(paths)
print(math.lcm(*paths.values()))

