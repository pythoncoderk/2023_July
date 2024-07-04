n = int(input())

for i in range(n):
    name, age, birth, state = map(str, input().split())
    print("User{")
    print(f"nickname : {name}")
    print(f"old : {age}")
    print(f"birth : {birth}")
    print(f"state : {state}")
    print("}")





