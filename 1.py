def sumIntervals(list): 
    tmp = []
    for l in list:
        x =int(l[0])
        x = x+ 1
        while x <= int(l[1]): 
            if x not in tmp:
                tmp.append(x)
            x = x+1
    return len(tmp)


print("Please give the numbers space seperated: ")
l=[]
tmp =[]
inp2 = input() # diavasma ari8mwn

inp = []
inp = inp2.split(' ') #split twn kenwn
count = 0
for x in inp:  # eisagwgh tous sth lista ana diades
    count = count+1
    tmp.append(x)    
    if(count%2 is 0):
        count = 0
        l.append(tmp)
        tmp = []

#sumIntervals( [[1,2], [6, 10], [11, 15] ] ) Επιστρέφει 9
result = sumIntervals(l) 
print(result)
