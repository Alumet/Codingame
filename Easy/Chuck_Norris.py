message = input()
code=''

for l in message:
    code+= bin(ord(l))[2:].zfill(7)# turn letter into bin

curent_nb=code[0]

if code[0]=='1': 
    answer='0 '
else:
    answer='00 '
    

for i in range (len (code)):
    
    if code[i]!=curent_nb:
        
        if code[i]=="1":
            if i==0:
                answer+="0 "
            else:
                answer+=" 0 "
                
        if code[i]=="0":
            if i==0:
                answer+="00 "
            else:
                answer+=" 00 "
        curent_nb=code[i]
        
    if code[i]==curent_nb:
        answer+="0"
        
print (answer)
