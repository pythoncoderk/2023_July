import math


A, B = map(int, input().split())



def minimum_attacks(A, B):
    return math.ceil(A / B)


print(minimum_attacks(A, B))
