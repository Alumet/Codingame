'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

elevator=[[-1,-10]]

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator.append([int(j) for j in input().split()])
    
elevator.append([exit_floor, exit_pos])
elevator.sort() 

# game loop
while 1:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    el_pos_1=elevator[clone_floor][1]
    el_pos_2=elevator[clone_floor+1][1]
    
    # action: WAIT or BLOCK
    if clone_pos==width-1 and direction=='RIGHT':
        print("BLOCK")
    elif clone_pos==0 and direction=='LEFT':
        print("BLOCK")
    elif clone_pos in [el_pos_1+1] and clone_pos-el_pos_2>0:
        print("BLOCK")
    elif clone_pos in [el_pos_1-1] and clone_pos-el_pos_2<0:
        print("BLOCK")
    else:
        print("WAIT")
