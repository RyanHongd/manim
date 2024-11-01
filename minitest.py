import math
n1=12345
list1 = []
t = math.floor(math.log10(abs(n1))) + 1
for i in range(t):
    digit = (n1 // (10 ** i)) % 10
    list1.insert(0, digit)
print(list1)





