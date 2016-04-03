
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

Link_table = {None : 'UNKNOWN'}

# Fill the dic
for i in range(n):
    ext, mt = input().split()
    Link_table[ext.lower()]=mt
    

for i in range(q):
    fname=(input().lower().split("."))
    
    if len(fname) > 1:
        answer=fname[-1]
    else:
        answer=None
        
    print(Link_table.get(answer, "UNKNOWN"))
