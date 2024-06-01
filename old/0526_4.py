s = input()

stack = []
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i+1)
    elif s[i] == ")":
        print(stack.pop(), i + 1)