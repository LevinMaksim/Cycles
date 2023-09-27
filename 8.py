A = int(input())
B = 0
C = 1
while A > 0:
    D = A % 10
    B += D
    C *= D
    A //= 10
print("Summ:", B)
print("Multi:", C)
