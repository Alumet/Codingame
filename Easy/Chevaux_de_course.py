'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

n = int(input())
power=[]

for i in range(n):
    pi = int(input())
    power.append(pi)

power.sort()

best=abs(power[1]-power[0])

for i in range(n-1):
    best = min( best, abs(power[i]-power[i+1]))

print (best)
