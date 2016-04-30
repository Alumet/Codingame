'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_X,thor_Y=initial_tx, initial_ty

# game loop
while 1:
    remaining_turns = int(input())

    direction_X=direction_Y=""
    
    if thor_X>light_x:
        direction_X="W"
        thor_X-=1
        
    elif  thor_X<light_x:
        direction_X="E"
        thor_X+=1
        
    if thor_Y>light_y:
        direction_Y="N"
        thor_Y-=1
        
    elif thor_Y<light_y:
        direction_Y="S"
        thor_Y+=1
    
    print (direction_Y+direction_X)
