'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

n = int(input())
liste=[]
for i in range(n):
    liste.append(input())
    
letters = input()
points=[(1,'eaionrtlsu'),(2,'dg'),(3,'bcmp'),(4,'fhvwy'),(5,'k'),(8,'jx'),(10,'qz')]

good_liste=[]
for w in liste:
    
    if set(w)-set(letters)==set():
        
        res_1=[(x,letters.count(x)) for x in (set(letters)&set(w))]
        res_2=[(x,w.count(x)) for x in set(w)]
        
        w_good=True
        for i in range(len(res_2)):
            if res_2[i][1]>res_1[i][1]:
                w_good=False
        
        if w_good:
            score=0
            for l in res_2:
                for p in points:
                    if l[0] in p[1]:
                        score+=p[0]
                        
            good_liste.append((score,w))

good_liste.sort(reverse=True,key=lambda val: val[0])
print(good_liste[0][1])
