'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]

line=[]
for i in range(h):
    line.append(input().split(' '))  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

left_type=["10"]
right_type=["11"]
down_type=["1","3","7","8","9","12","13"]
horizontal_type=["2","6"]
special_type=["4","5"]

# game loop
while 1:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.ft["10"]
    tile=line[yi][xi]
    
    if line[yi][xi] in left_type:
        xi-=1
        direction="left"
    elif line[yi][xi] in right_type:
        xi+=1
        direction="right"
    elif line[yi][xi] in down_type:
        yi+=1
    elif line[yi][xi] in horizontal_type:
        if direction=="left":
            xi-=1
        if direction=="right":
            xi+=1
    elif line[yi][xi]==special_type[0]:
        if old_tile in down_type or direction=="down":
            xi-=1
            direction="left"
        else:
            yi+=1
            dierction="down"
    elif line[yi][xi]==special_type[1]:
        if old_tile in down_type or direction=="down":
            xi+=1
            direction="right"
        else:
            yi+=1
            direction="down"
        
    old_tile=tile
    print(xi,yi)
