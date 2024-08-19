n = int(input())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

answer = sorted(s1 | s2)
print(*answer)