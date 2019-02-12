print("Dwste to onoma tou arxeiou")
FileNale = input()  
with open(FileNale) as f:
    Lines = f.readlines()

#print (content)
toPrint = ""
for x in Lines: # iterate all lines
    str = x
    for i in range(0,len(str)):# iterate line by line
        if str[i]=='#':            
            toPrint +='\n'
            break
        else:
            toPrint += str[i]           
#
#for j in range(0,len(toPrint)):    
 #   print (toPrint[j],end='')

print (toPrint,end='') # maybe write it to a file??