
n = eval(input())
kn = input()
k = kn.strip().split(" ")
int_k = []
for i in k:
    int_k.append(int(i))
int_k.sort()
print(int_k[n-1])