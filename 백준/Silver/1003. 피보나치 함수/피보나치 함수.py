import sys

input = sys.stdin.readline
a = int(input())
for _ in range(a):
    n = int(input())
    fibo = {0: [1, 0], 1: [0, 1]}
    for i in range(2, n + 1):
        fibo[i] = [fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1]]
    for j in fibo[n]:
        print(j, end=" ")
    print()