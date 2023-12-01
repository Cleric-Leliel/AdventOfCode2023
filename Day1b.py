#Advent of Code 2023
#Day 1: Calibration string fixes
#part 2: Include spelled digits
#v1.0  12-01-2023

with open('Day1in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0

validdig = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9} #"zero" not found in puzzle input
validstart = ["o","t","f","s","e","n"]


for i in range(0,len(read_data)):
    comb =0
    j=0
    while j < len(read_data[i]):   #check forward from 1
        char = read_data[i][j]
        if char.isdigit():         
            comb = int(char) * 10
            j = len(read_data[i])   #done
        elif char in validstart:
            if (len(read_data[i])-j )>=5:
                word = read_data[i][j:j+5]
            else:
                word = read_data[i][j:]
            if word.find("twone")>= 0:   #special case - doesnt actually cause an issue due to dict order
                         comb = 20
                         j = len(read_data[i]) #done
            else :
                j = j+1
                for x in validdig.keys():
                    if word.find(x)>= 0:
                        comb = validdig[x] * 10                        
                        j = len(read_data[i])   #done
                        if word[1].isdigit():  # fix special case like 'e3two'
                            comb = int(word[1]) * 10
                            #print(validdig[x]," in  ", word.strip(), " ",comb)
                
        else:
            j = j+1

    j = len(read_data[i])-1
    while j >=0:                     #Check backward from end
        char = read_data[i][j]
        if char.isdigit():         
            j = -1             #done
            comb = comb + int(char)
        elif char in validstart:
            word = read_data[i][j:]  #dont need to limit window length moving backwards
            for x in validdig.keys():
                if word.find(x)>= 0:
                    comb = comb + validdig[x]
                    j = -1 #done  
        j = j-1


    if comb < 11:
        print("\nERROR: INVALID RESULT\n")
    
        
    sumtot = sumtot+comb
    #print(i+1,"  ",read_data[i].strip(),"    comb: ",comb,"   subtot: ",sumtot)
    
print("sumtot: ",sumtot)


