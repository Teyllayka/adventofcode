import numpy as np

f = open("nums.txt","r")
c_data = f.read().split('\n')


num_array = c_data[0].split(',')
c_data.pop(0)
c_data = [x for x in c_data if x != '']
c_data = [x.split() for x in c_data]
c_data = sum(c_data, [])
lenght = len(c_data)/25
c_data = np.array(c_data, int).reshape(int(lenght), 5, 5)
board_index = bk_num = 0
break_flag = False
completed_boards = []

for a in num_array:
  if break_flag:
    break
  if int(a) in c_data:
    result = np.where(c_data==int(a))
    cords= list(zip(*result))
    for i in range(len(cords)):
      c_data[cords[i]] = 999
  for z in range(int(lenght)):
    if break_flag:
      break
    if np.any(np.all(c_data[z] == 999, axis=0)) or np.any(np.all(c_data[z] == 999, axis=1)):
      if not z in completed_boards:
        completed_boards.append(z)
      if len(completed_boards) == int(lenght):   
        board_index = z
        break_flag = True
        bk_num = int(a)

print(bk_num)
print(len(completed_boards))
winner = c_data[board_index]
print(winner)
print(sum(winner[winner != 999])*bk_num)
