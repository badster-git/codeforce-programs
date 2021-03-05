w = int(input())
if (w % 2 == 0) and ((w <= 100) and (w > 2)):
    for i in range(2,w,2):
        if ((2 + i) == w):
            print('YES')
else:
    print('NO')
