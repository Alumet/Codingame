'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

n = int(input())
liste=[]
for i in range(n):
    j, d = [int(j) for j in input().split()]
    liste.append([j,j+d-1])
    
liste.sort(key=lambda x: x[0])
liste.sort(key=lambda x: x[1])

J_max=0
count=0

for el in liste:
    if el[0]>J_max:
        J_max=el[1]
        count+=1
      
print(count)
