import math

lon = float(input().replace(",","."))
lat = float(input().replace(",","."))
n = int(input())
defib=[]

for i in range(n):
    data=input()
    data=data.replace(",",".")
    defib.append(data.split(";"))

best_d=1e1000

for obj in defib:
    lon_def,lat_def= float(obj[4]),float(obj[5])
   
    X=(lon_def-lon)*math.cos(lon_def+lon/2)
    Y=(lat_def-lat)
    d=(X**2+Y**2)**(1/2)*6371

    if d<best_d:
       best_d=d
       best_name=obj[1]
   
print(best_name)
