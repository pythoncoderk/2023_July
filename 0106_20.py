n = int(input())
s = input()
t = input()

s_l = [ord(i)-96 for i in s]
t_l = [ord(i)-96 for i in t]
i = 0
good_l = [s_l[i] + 28 - n for i in range(n)]
good_l2 = [good_l[i] if good_l[i] <= 26 else good_l[i] - 26 for i in range(n)]
print(s_l)
print(good_l2)
print(t_l)

final = [1 if good_l2[i] == t_l[i] else 0 for i in range(n)]
print(final)

if len(final) == final.count(1):
    print("")
