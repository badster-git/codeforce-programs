i, total, days = 0

def check(a, b):
    if i == 0:
        if ((a >= 1 and a <= 30) and (b >= 0 and b <= 240)):
            days = a
            total = b
            i += 1
            pass
        else:
            i = 0
            print('NO')
    if i > 0:
        if ((0 <= a and a <= b and b <= 8):
            for x in range(a, b):
                if x * days == total:
                    print('YES')

            i += 1



