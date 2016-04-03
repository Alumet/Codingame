
l, c, n = [int(i) for i in input().split()]
groupes=[]
loop_g=[]
loop_m=[]
looping=True

for i in range(n):
    groupes.append([i,int(input())])
    
result=0
j=0
while j < c:

    load=0
    sub_group=[]
    for i in range (n):
        
        if l-load>=groupes[0][1]:
            
            load+=groupes[0][1]
            groupes.append(groupes.pop(0))
            sub_group.append(groupes[0][0])

    
    if sub_group in loop_g and looping:
        
        D_gain=result-loop_m[loop_g.index(sub_group)][0]
        D_loop=(j-loop_m[loop_g.index(sub_group)][1])
        
        repeat=int((c-j)/D_loop)
        result+=int(D_gain*repeat)
        
        j=D_loop*(repeat+1)+loop_m[loop_g.index(sub_group)][1]+1
        
        if j<=c:
            result+=load

        looping=False
        
    else:
        
        loop_g.append(sub_group)
        loop_m.append([result,j])
        result+=load
        j+=1

print(result)
        
