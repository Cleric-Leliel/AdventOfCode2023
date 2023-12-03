#Advent of Code 2023
#Day 3: Gear Ratios 
#v1.0  12-03-2023

import re

with open('Day3in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0
partsdb = {}
maxcol = len(read_data[0]) -2   #or strip trailing whitespace
maxrow = len(read_data) -1

#build dict of parts and their locations
for i in range(0,len(read_data)):
    for part in re.finditer(r'\d+', read_data[i] ):
        keyID = part.group()+"-"+str(i)+"-"+str(part.start(0))  #added coord to keyID for uniqueness
        partsdb.update({keyID: [i, part.start(0), part.end(0)-1,part.group()]}) # dict of form { part no : [ row, col1, col2 ] }

#search for symbols near part num loc
for p in partsdb.keys():
        row = partsdb[p][0]  #e.g., i
        col1 =partsdb[p][1]    
        col2 =partsdb[p][2]
        for x in (col1-1, col2+1):      #check left and right
            if read_data[row][x] != '.'  and x >= 0 and x <= maxcol:  
                #print(p, "validated by adjacent symbol at [",row, x, "]")
                sumtot = sumtot + int(partsdb[p][3])
                break
        for y in (row-1, row+1):        #above and below
                x1 = max(col1-1,0)
                x2 =min(col2+1,maxcol)      #one before and 1 after for diags
                if y>= 0 and y<=maxrow:   #skip edges
                    word = read_data[y][x1:x2+1]
                     sym =re.findall(r"([\-#$*+=_@/%&]+)",word)
                    if  sym != []: 
#                       print(p, "validated at row [" , y ,"], by ",sym,)
                        sumtot = sumtot + int(partsdb[p][3])
                        break
            
#print(partsdb)
                               
print("sumtot: ",sumtot)
