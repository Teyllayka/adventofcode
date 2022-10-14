f = open("input.txt","r")
data = f.read()
c_data = data.split('\n')
f.close

one = zero = 0
gamma = epsilon = c_data


for i in range(12):
  if len(gamma) == 1:
    break
  for a in range(len(gamma)):  
    if gamma[a][i] == "0":
      zero += 1
    elif gamma[a][i] == "1":
      one += 1
  if zero > one:
    gamma = list(filter(lambda a: a[i] == '0', gamma))
  else:
    gamma = list(filter(lambda a: a[i] == '1', gamma))
  zero = one = 0  
  if len(epsilon) == 1:
    break
  for a in range(len(epsilon)):  
    if epsilon[a][i] == "0":
      zero +=1
    elif epsilon[a][i] == "1":
      one +=1
  if zero > one:
    epsilon = list(filter(lambda a: a[i] == '1', epsilon))
  else:
    epsilon = list(filter(lambda a: a[i] == '0', epsilon))
  zero = one = 0 

print(int(gamma[0], 2)*int(epsilon[0], 2))