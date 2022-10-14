f = open("nums.txt","r")
c_data = f.read().split('\n')
c_data = [int(i) for i in c_data]

n = 0
for i in range(1, len(c_data)-2):
  if c_data[i-1] + c_data[i] + c_data[i+1] < c_data[i] + c_data[i+1] + c_data[i+2]:
    n+=1
print(n)