#Advent of Code 2023
#Day 4: Scratchcards 
#v1.0  12-04-2023

import re

with open('Day4in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot=0

for i in range(0,len(read_data)):
   card =0
   pt = 1
   cardID, winners, scratch =re.split(': |\| ',read_data[i].strip())
   winners =re.split(' |  ', winners)  #convert to list
   scratch = re.split(' |  ', scratch)  #convert to list

   for n in scratch:
       if n in winners and n != "":
           #print("winner :", n, "pts = ",pt )
           card = pt
           pt = pt * 2

   #print(cardID, card)        
   sumtot = sumtot + card
                               
print("sumtot: ",sumtot)
