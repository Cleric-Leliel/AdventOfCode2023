#Advent of Code 2023
#Day 3: Gear Ratios
#part 2 - Gears (part 1 should really have been "parts shopping")
#v1.0  12-03-2023

import re

with open('Day3in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0
partsdb = {}
gears={}
maxcol = len(read_data[0]) -2   #or strip trailing whitespace
maxrow = len(read_data) -1

#build dict of parts and their locations
for i in range(0,len(read_data)):
    for part in re.finditer(r'\d+', read_data[i] ):
        keyID = part.group()+"-"+str(i)+"-"+str(part.start(0))  #added coord to keyID for uniqueness
        partsdb.update({keyID: [i, part.start(0), part.end(0)-1,part.group()]}) # dict of form { part#-y-x : [ row, col1, col2,part# ] }

#search for symbols near part num loc
for p in partsdb.keys():
        row = partsdb[p][0]  #e.g., i
        col1 =partsdb[p][1]    
        col2 =partsdb[p][2]
        for x in (col1-1, col2+1):      #check left and right
            if read_data[row][x] == '*'  and x >= 0 and x <= maxcol:
                symID = "*"+str(row)+"-"+str(x)
                symval = int(partsdb[p][3])  #part number
                if symID in gears.keys():                                                                           
                    gearlist = gears[symID]
                    gearlist.append(symval)
                    gears.update({symID: gearlist})
                else:
                    gears.update({symID: [symval]})
                
                #print(p, "validated by adjacent symbol at [",row, x, "]"))
                break
        for y in (row-1, row+1):        #above and below
                x1 = max(col1-1,0)
                x2 =min(col2+1,maxcol)      #one before and 1 after for diags
                if y>= 0 and y<=maxrow:   #skip edges
                    word = read_data[y][x1:x2+1]
                    sym =word.find("*")
                    if  sym >= 0: 
#                       print(p, "validated at row [" , y ,"], by ",sym,)
                        symID = "*"+str(y)+"-"+str(x1+sym)
                        symval = int(partsdb[p][3])  #part number                              #not a fan of this duplication
                        if symID in gears.keys():
                            gearlist = gears[symID]
                            gearlist.append(symval)
                            gears.update({symID: gearlist})
                        else:
                            gears.update({symID: [symval]})
                        break
            
            
for g in gears.keys():
    if len(gears[g]) == 2:
        sumtot = sumtot + (gears[g][0] * gears[g][1])
#print(partsdb)
#print(gears)
                               
print("sumtot: ",sumtot)
