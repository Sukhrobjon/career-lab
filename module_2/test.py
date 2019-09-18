def num(c):
    return ord(c) - ord('A') + 1

c = 'AD'

x = num(c[0]) * 26
y = num(c[1])

n = x + y
print(n)