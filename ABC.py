# A B C D E 
# B C D E F 
# C D E F G 
# D E F G H 
# E F G H I 

i=0
while i<5:
    j=0
    k=ord("A")+i
    while j<5:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1