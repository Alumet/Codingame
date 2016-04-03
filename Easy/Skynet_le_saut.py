
road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.
    
    V_ideal=gap+1
    
    if (road-coord_x)>1:
        if speed<V_ideal:
            print("SPEED")
        elif speed>V_ideal:
            print("SLOW")
        else:
            print("WAIT")
    elif (road-coord_x) in range (1,2):
        print("JUMP")
    else:
        print("SLOW")
