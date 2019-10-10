n = int(input('Dame la n: '))
  
# Initialize matrix 
matrix = [] 
# print("Enter the entries rowwise:") 

# For user input 
for i in range(n):          # A for loop for row entries 
    a =[] 
    for j in range(n): 
         # A for loop for column entries 
        if(j == 0 or j == n-1):
            a.append(int(1)) 
        elif(i == 0 or i == n-1):
            a.append(int(1))
        else:
            a.append(int(0))
    matrix.append(a) 
  
# For printing the matrix 
for i in range(n): 
    for j in range(n): 
        print(matrix[i][j], end = " ") 
    print() 