
k,n = map(int,input().split())

for i in range(n):
    if k <= 50:
        interest = k//10
        k += interest+5
    else:
        k += 5+5

print(k)
