l = [1, 2, 3, 4, 5]
loop = 2
for i in range((len(l)*2) - 1):
    if i < len(l):
        print(l[i])
    else:
        print(l[i - loop])
        loop += 2