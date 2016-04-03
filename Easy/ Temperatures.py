input()
raw_temps = input() or '0'

temps_int = [int(x) for x in raw_temps.split()]# return list of int
temps_int.sort(key = lambda x: (abs(x),-x))#sort around 0

print(temps_int[0])
