A = int(input())
B = 0
while A > 0:
    C = A % 10
    if B % 2 == 0:
        B += C
    A //= 10
print(C)
