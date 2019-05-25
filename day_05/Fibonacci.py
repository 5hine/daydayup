list = [1, 1]
for i in range(2,100):
    list.append(list[i-2]+list[i-1])
print(list)

# 法2
a = 0
b = 1
while b<1000:
    print("%d "%b,end="")
    a, b = b, a + b