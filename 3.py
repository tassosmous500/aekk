def maxSublistaaySum(lista):

    max_so_far = lista[0]
    curr_max = lista[0]
    numbers= [] #holds the sublist with the biggest sum

    for i in range(1,len(lista)):
        curr_max = max(lista[i], curr_max + lista[i])
        max_so_far = max(max_so_far,curr_max) #this holds the biggest sum
    print(max_so_far,": ",end="")
    tmp = 0

    for i in range(0,len(lista)): #searching for the sub list        
        if tmp == max_so_far: 
                return(numbers)
        else:
            numbers.clear()
            tmp = 0
        for j in range(i,len(lista)):#starts from lista[j] adding until we find the max_so_far
            tmp += lista[j]
            numbers.append(lista[j])
            if tmp == max_so_far:#if max sum found break
                break
                
print("Dwste me keno tous arithmous ths listas:")
lista = list(map(int, input().split())) # read the ints

print(maxSublistaaySum(lista))