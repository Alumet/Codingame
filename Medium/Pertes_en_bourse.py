'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

n = int(input())
values = [int(x) for x in input().split(" ")]
    
loss,Max=0,0

for price in values:

    Max = max(Max, price)
    loss = min(loss, price - Max)
    
print(loss)
