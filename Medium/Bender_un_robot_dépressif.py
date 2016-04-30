'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c = [int(i) for i in input().split()]
Map=[]
T=[]
for i in range(l):
    Map.append(input())
    if "@" in Map[i]:
        X=Map[i].index('@')
        Y=i
    if 'T' in Map[i]:
        T.append([Map[i].index('T'),i])
        
direction_loop=['S','E','N','W']
direction_values=[('S',0,1),('N',0,-1),('E',1,0),('W',-1,0)]
direction=('S',0,1)

def heading():
    for i in direction_loop:
        direction=heading_value(i)
        if Map[Y+direction[2]][X+direction[1]] in [' ','S','E','N','W','T','I','B','$']:
            return direction
            break
            
def heading_value(x):
    for i in direction_values:
        if x==i[0]:
            return i
            
mv_liste=[]
going=True
beer=False
loop=False
c=0

while going:

    if Map[Y][X]=="B":
        if beer:
            beer=False
        else:
            beer=True
            
    if Map[Y][X]=="I":
        direction_loop.reverse()
    
    if Map[Y][X]=="T":
        for el in T:
            if el!=[X,Y]:
                X=el[0]
                Y=el[1]
                break
    
    if Map[Y][X]=="$":
       going=False
    
    else:
        X_t1=X+direction[1]
        Y_t1=Y+direction[2]
        
        if Map[Y][X] in ['S','N','E','W']:
            direction=heading_value(Map[Y][X])
            
        elif Map[Y_t1][X_t1]=='#':
            direction=heading()
        elif Map[Y_t1][X_t1]=='X':
            if beer:
                Map[Y_t1]=Map[Y_t1][0:X_t1]+' '+Map[Y_t1][X_t1+1::]
            else:
                direction=heading()
    
        X+=direction[1]
        Y+=direction[2]

        if [direction[0],(X,Y)] in mv_liste:
            c+=1
            if c>len(mv_liste)/1.2:
                
                loop=True
                going=False
            
        mv_liste.append([direction[0],(X,Y)])

    
trad=['SOUTH','EAST','NORTH','WEST']
direction_loop=['S','E','N','W']

if loop:
    print("LOOP")
else:
    for el in mv_liste:
        print(trad[direction_loop.index(el[0])])
