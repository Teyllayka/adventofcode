f = open("nums.txt","r")
c_data =  f.read().split('\n')
b = 0


for i in range(len(c_data)): # very cringy 
  for a in range(len(c_data)): # very cringy 
    for c in range(len(c_data)): # very cringy 
      if int(c_data[i]) + int(c_data[a]) + int(c_data[c]) == 2020: # very cringy 
        b = int(c_data[i]) * int(c_data[a]) * int(c_data[c]) # very cringy 




print(b)