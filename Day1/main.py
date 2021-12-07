
LIST = open("input.txt").read().split()
################DAY ONE LEVEL 1########################

#solution 1
def dayOneLevelOne(list):
 soluce = 0
 for x,y in zip(list, list[1:]):
   if (x < y):
     soluce += 1
 print(soluce)

print(dayOneLevelOne(LIST))

################DAY ONE LEVEL 2########################

#solution 2.1 : [RESULT :1705] 
def dayOneLeveltwo(myList):
 soluce = 0
 for x, y in zip(myList, myList[3:]):
   if x < y:
     soluce +=1
 return soluce

#solution 2.2 [RESULT :1755]
def dayOneLeveltwo(myList):
 soluce = 0
 for x in range(len(myList)-3):
   comp1 = myList[x] + myList[x+1] + myList[x+2]
   comp2 = myList[x+1] + myList[x+2] + myList[x+3]
   if comp1 < comp2:
     soluce +=1
 return soluce

#solution 2.3 : [RESULT :1755]
def dayOneLeveltwo(myList):
  soluce = 0
  for x in range(len(myList)-3):
    if myList[x] < myList[x+3]:
      soluce += 1
  return soluce

print(dayOneLeveltwo(LIST))

######################################################
