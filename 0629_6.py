n = int(input())

if n == 0:
    print(444)

n = min(n,6)
ans = 'No'
if pow(2,n) > n*n:
    ans = 'Yes'
print(ans)