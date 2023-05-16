import numpy as np

f = open("nums.txt","r")
c_data = f.read().split(',')

c_data = [int(a) for a in c_data]

for d in range(80):
  for i in range(len(c_data)):
      c_data[i] -= 1
      if c_data[i] < 0:
          c_data[i] = 6
          c_data.append(8)



print(len(c_data))