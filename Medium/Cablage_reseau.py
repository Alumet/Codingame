
n = int(input())

X,Y=[],[]
coord=[]
for i in range(n):
    x, y = [int(j) for j in input().split()]
    X.append(x)
    Y.append(y)
    coord.append([x,y])

X.sort()
Y.sort()
cable_length=X[n-1]-X[0]


for i in range (n):

    if n%2==1:
        Med=int((n-1)/2)
        cable_length+=abs(coord[i][1]-Y[Med])
    
    else:
        Med=int(n/2)
        Y_med=int((Y[Med-1]+Y[Med+1])/2)
        cable_length+=abs(coord[i][1]-Y_med)

print(int(cable_length)) 
