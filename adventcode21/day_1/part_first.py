f = open("nums.txt","r")
c_data = f.read().split('\n')

n = 0
for i in range(1, len(c_data)):
  if int(c_data[i]) > int(c_data[i-1]): n+=1
  
print(n)