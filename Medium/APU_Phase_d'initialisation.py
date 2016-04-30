'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
line=[]

for i in range(height):
    line.append(input()) # width characters, each either 0 or .


for y1 in range (height):
    for x1 in range(width):
        if line[y1][x1]=="0":
            
            if x1==width-1:
                x2,y2=-1,-1
            else:
                found=False
                for x1_b in range(x1+1,width):
                    if line[y1][x1_b]=="0" and found==False:
                        x2,y2=x1_b,y1
                        found=True
                if found==False:
                    x2,y2=-1,-1
            
            if y1==height-1:
                x3,y3=-1,-1
            else:
                found=False
                for y1_b in range(y1+1,height) :
                    if line[y1_b][x1]=="0"and found==False:
                        x3,y3=x1,y1_b
                        found=True
                if found==False:
                    x3,y3=-1,-1
                
            print(x1,y1,x2,y2,x3,y3)
