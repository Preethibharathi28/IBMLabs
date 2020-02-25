x=[[12,7,3],
   [3,5,7],
   [23,6,9]]
y=[[6,8,5],
   [4,8,2],
   [6,9,3]]
result=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for  i in result:
    print(i)
