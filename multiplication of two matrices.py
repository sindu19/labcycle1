X = [[1,3,2],
    [3 ,6,8],
    [5 ,2,1]]

Y = [[6,8,6],
    [6,3,3],
    [2,5,1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
    for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
