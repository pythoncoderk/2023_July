n = int(input())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
final_l = [l2[i] - l1[i] for i in range(n)]

print(*final_l)