'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

graph = {}
gates = []

N, L, E = [int(i) for i in input().split()]

for i in range(N):
    graph[i] = []

for i in range(L):
    Node_1, Node_2 = [int(i) for i in input().split()]
    graph[Node_1].append(Node_2)
    graph[Node_2].append(Node_1)
    
for i in range(E):
    gate = int(input())
    gates.append(gate)


# game loop
while 1:
    SI = int(input())
    neighbours = graph[SI]
    action =  str(SI)+' '+ str(neighbours[0])
    
    for node in neighbours :
        if node in gates:
            action = str(SI)+' '+ str(node)
            break
        
    print(action)
