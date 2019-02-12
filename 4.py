import sys

mysums = [] # keeps all the sums

def subsetSums(lista, l, r, sum = 0):     
    
    if l > r: 
        mysums.append(sum)   
        return 
    # Subset me lista[l] 
    subsetSums(lista, l + 1, r, sum + lista[l]) 
    # Subset xwris lista[l] 
    subsetSums(lista, l + 1, r, sum)

def calculateSums(lista):    
    mylen = len(lista)
    sums = []
    for i in range(0,(1<<mylen)):
        sum = 0
        for j in range(0,mylen):
            if i & (1<<j):
                sum += lista[j]
        sums.append(sum)
    print("to sums einai: ",sums)
    print ("to sums len einai: ",len(sums))

def maxDistance(lista, max):      
  subsetSums(lista,0,len(lista)-1) #stores all the sums into mysums
  mysums.sort(reverse=True) # sorting the list in descending order
  isFound = False # flag gia elegxo oti bre8ike a8roisma mikrotero tou int pou edwse o xrhsths
  for x in mysums:
      if(x <= max and x != 0):
          print("to megalutero athroisma einai: ",x)
          isFound = True
          break
  if (isFound == False):
       print("O akereos pou dothike einai mikroteros apo ola ta athroismata")
 
print("Dwste me keno tous arithmous ths listas:")
#lista = input()
lista = list(map(int, input().split())) # read the ints
print("Dwste ton thetiko akeraio")
max =  int(input())
if max < 0:
   print("Error Dwste thetiko ari8mo")
   sys.exit()

maxDistance(lista,max)
