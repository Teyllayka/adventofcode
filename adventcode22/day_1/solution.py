import itertools
f = open("input.txt", "r")
data = [' ' if item == '' else item for item in f.read().split('\n')]
result = [list(v)for k, v in itertools.groupby(data, key=str.isspace) if not k]
print(result)
