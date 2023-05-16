f = open("input.txt","r")
data = f.read()
c_data = data.split('\n')
f.close

one = 0
zero = 0
gamma = ''
epsilon = ''

for i in range(len(c_data[0])):
  for a in range(len(c_data)):
    if c_data[a][i] == "0":
      zero +=1
    elif c_data[a][i] == "1":
      one +=1
  if zero > one:
    gamma += '0'
    epsilon += '1'
  elif one > zero:
    gamma += '1'
    epsilon += '0'
  zero = one = 0
print(int(gamma, 2)*int(epsilon, 2))