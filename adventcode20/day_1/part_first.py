f = open("nums.txt","r")
c_data =  f.read().split('\n')
b = 0


for i in range(len(c_data)):
  for a in range(len(c_data)):
    if int(c_data[i]) + int(c_data[a]) == 2020:
      b = int(c_data[i]) * int(c_data[a])




print(b)