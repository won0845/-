import sys
input = sys.stdin.readline

n, k, l =map(int, input().split())
lst = []
hap = 0

for i in range(n):
    a, b, c = map(int, input().split())
    if a < l or b< l or c<l:
        continue
    if a+b+c >= k:
        lst.extend([a,b,c])

print(len(lst)//3)
print(*lst)