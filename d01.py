with open('d01.in') as f:
    data = f.read()
dig = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
data = data.splitlines()
s = 0
for line in data:
    f = lst = x = 0
    for i in range(len(line)):
        if line[i] > '9':
            for j, k in enumerate(dig):
                if line[i:].startswith(k):
                    x = j + 1
        else:
            x = int(line[i])
        if f == 0:
            f = x
            continue
        lst = x
    if lst == 0:
        lst = f
    s += 10 * f + lst
print(s)
