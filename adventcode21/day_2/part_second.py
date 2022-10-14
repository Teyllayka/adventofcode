f = open("movement.txt","r")
c_data = f.read().split('\n')

height = lenght = aim = 0


for i in c_data:
  match i.split()[0]:
    case 'forward':
        lenght += int(i.split()[1])
        height += aim * int(i.split()[1])
    case 'up':
        aim -= int(i.split()[1])
    case 'down':
        aim += int(i.split()[1])

print(lenght*height)