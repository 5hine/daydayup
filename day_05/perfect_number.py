
for i in range(2,100):
    sum = 1
    for j in range(2,100):
        if j < i and i % j == 0:
            sum += j
    if sum == i:
        print("%d 是完美数"%i)