for i in range(1,5):
    for j in range(1,5):
        print(i,j)
#print the * patten but the rows count gives you user
rows = int(input("Enter the rows ->"))
for i in range(1,rows + 1):
    for j in range(1 ,i + 1):
        print("*",end="")
    print()    
# print patten question 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
rows = int(input("Enter the rows no ->"))
for i in range(1,rows + 1):
    for j in range(1,i+1):
        print(j,end=" ")
    
    print()    
# print patten question like take the input from the user
# 1
# 1 2 1 
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
rows =int(input("Enter the rows ->"))
for i in range (1,rows + 1):
    for j in range (1,i+1):
        print(j,end="")
    for k in range (i - 1,0,-1):
        print(k,end="")
    print()    
                             