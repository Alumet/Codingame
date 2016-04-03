l = int(input())
h = int(input())
t = input()

row=[]
for i in range(h):
    row.append(input())

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

letter=[]
for obj in t:
    found=False
    for i in range(len(alpha)):
        if obj.lower()==alpha[i]:
            letter.append(i)
            found=True
            
    if found==False:
        letter.append(len(alpha))

for i in range (h):
    string=""
    for obj in letter:
       string+=row[i][obj*l:obj*l+l]
    print(string)
