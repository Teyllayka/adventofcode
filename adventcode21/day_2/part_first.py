f = open("movement.txt","r")
c_data = f.read().split('\n')

height = lenght = 0

for i in c_data:
  match i.split()[0]:
    case 'forward':
        lenght += int(i.split()[1])
    case 'up':
        height -= int(i.split()[1])
    case 'down':
        height += int(i.split()[1])
print(lenght*height)