def xor(a, b):
    return (a and not b) or (not a and b)


c = xor(1, 2)
print(c)
a = "001010"
b = "111111"
y = 2 ^ 1
print("{0:b}".format(y))
