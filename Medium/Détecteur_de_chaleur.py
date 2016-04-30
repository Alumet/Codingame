'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

pose_x_max=w
pose_x_min=0
pose_y_max=h
pose_y_min=0

# game loop
while 1:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "D"in bomb_dir:
        pose_y_min=y0
    elif "U" in bomb_dir:
        pose_y_max=y0
    if "L" in bomb_dir:
        pose_x_max=x0
    elif "R" in bomb_dir:
        pose_x_min=x0
    
    x0=int((pose_x_max+pose_x_min)/2)
    y0=int((pose_y_max+pose_y_min)/2)
    
    print(x0,y0)
    
