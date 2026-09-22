# print pair of the question 1 to 5.
for i in range(1,6):
    for j in range(0,i):
        print(i,j+1)
# print * patten question like this->
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range (1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()  
# print this question in reverse method
# * * * * *
# * * * * 
# * * * 
# * *
# *
for i in range(6,0,-1):
    for j in range(i-1,0,-1):
        print("*",end="")
    print()       
#print the number rows wise like this
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1
# print this type of patten
for i in range(1,5):
    for j in range(1,i + 1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()    
