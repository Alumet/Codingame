'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

import sys
import math

l, h = [int(i) for i in input().split()]
numeral=[]
for i in range(h):
    numeral.append(input())
  
numeral_liste=[]
for i in range(20):
    temp=[]
    for j in range(h):
        temp.append(numeral[j][i*l:(i+1)*l])
    numeral_liste.append(temp)

s1 = int(input())
num_1=[]
for i in range(int(s1/l)):
    temp=[]
    for i in range(l):
        temp.append(input())
    num_1.append(temp)
    
s2 = int(input())
num_2=[]
for i in range(int(s2/l)):
    temp=[]
    for i in range(l):
        temp.append(input())
    num_2.append(temp)


operation = input()

def may_to_num(n):
    n.reverse()
    res=0
    for i in range(len(n)):
        res+=numeral_liste.index(n[i])*20**(i)
    return int(res)

def puiss(n):
    i=0
    p=20**1
    while p<=n:
        i+=1
        p=20**i
    if i>0:
        return i-1
    else:
        return i

def num_to_may(n):
    res=[]
    for i in range(puiss(n),-1,-1):
        num=int(n/20**i)
        res.append(numeral_liste[num])
        n-=num*20**i
    return res
    
n1=may_to_num(num_1)
n2=may_to_num(num_2)

if operation=="+":
    result=n1+n2
if operation=="-":
    result=n1-n2
if operation=="*":
    result=n1*n2
if operation=="/":
    result=n1/n2

result=num_to_may(result)

for l in result:
    for L in l:
        print(L)
