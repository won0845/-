import sys
input = sys.stdin.readline

x = []
y = []

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

print((x[-1] - x[0]) * (y[-1] - y[0]))