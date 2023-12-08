#Advent of Code 2023
#Day 7:Camel Cards
#v1.0  12-07-2023

import re
import math

with open('Day7in.txt') as f:
    read_data = f.readlines()
f.close()

sumtot = 0
maxrank = len(read_data)+1
hands ={}       #hand : bid
rankscore= {}   #hand : rankscore (an internal number)
rankscore_rev ={}

cardscore = {'A':14,'K':13,'Q':12 ,'J':11,'T':10}
#htypes = ["5x","4x","Full","3x","2Pair","1Pair","HighC"]
#No tie condition given; assume no ties
for i in range(0, len(read_data)):
    hand, bid = read_data[i].split()
    bid = int(bid)
    hands.update({hand: bid})

    #SET INITAL RANKNUM VALUE
    cnt = 0
    for x in hand:  #range(0, len(hand)-1):
        cnt = hand.count(x)
        if cnt == 5:               
            rankscore.update({hand:7000000})    #"5x
            break
        elif cnt == 4:
            rankscore.update({hand:6000000  })  #"4x"
            break
        elif cnt == 3:
            chkhnd = hand.replace(x,"")
            if chkhnd[0] == chkhnd[1]:
                 rankscore.update({hand:5000000 }) #Full
            else:
                 rankscore.update({hand:4000000})  #3x
            break   
        elif cnt ==2:  
             chkhnd = hand.replace(x,"")   # 3-char string
             cnt2 = hand.count(chkhnd[0])
             cnt3 =  hand.count(chkhnd[1])
             if cnt2 ==2 or cnt3 == 2:
                  rankscore.update({hand:3000000 })  #2Pair",
             else:
                 rankscore.update({hand:2000000  })  #"1Pair",
        else:
            if  hand not in  rankscore.keys():
                 rankscore.update({hand:1000000 })  #"HighC"

#TIEBREAKERS - Add ranknum by individual cards 
for j in rankscore:          #This is why the initial numbers have so many digits. Also considered using hex
    ranknum = rankscore[j]
 #   print(j, rankscore[j])
    m =  10000  #multiplier
    for k in j:
        if k.isdigit():
            ranknum =ranknum + (int(k) *m)
        else:
            ranknum = ranknum + (cardscore[k] *m)
        m = m /100
    rankscore.update({j:ranknum})
    rankscore_rev.update({ranknum:j})    

#Sort and Score
ranks  = sorted(rankscore_rev)  #gives sorted list of the keys

for z in range(0,len(ranks)):
    currhand = rankscore_rev[ranks[z]]
    #if z>900 and z< 1000:
    #    print(currhand, " has rank ",z+1, " with internal value  of", rankscore[currhand], "bid ",hands[currhand])
    score = (z+1) * hands[currhand]
    sumtot = sumtot+score

#print(ranks)
print("sum =",sumtot)

