#Advent of Code 2023
#Day 1: Calibration string fixes
#v1.0  12-01-2023

with open('Day1in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0
comb =0

for i in range(0,len(read_data)):
    j=0
    while j < len(read_data[i]):   #check forward from 1
        char = read_data[i][j]
        if char.isdigit():         
            #print("1st dig: ", char)
            j = len(read_data[i])
            comb = int(char) * 10
        else:
            j = j+1

    j = len(read_data[i])-1  
    while j >=0:                     #Check backward from end
        char = read_data[i][j]
        if char.isdigit():         
            #print("last dig: ", char)
            j = -1
            comb = comb + int(char)
        else:
            j = j-1

    #print("comb: ",comb)
    sumtot = sumtot+comb
    
print("sumtot: ",sumtot)


