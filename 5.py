One = int(input())
c, d = 0, 1
for _ in range(One):
    print(c, end=' ')
    rw = c + d
    c = d
    d = rw
