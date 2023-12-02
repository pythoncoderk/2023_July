def say(word, *args):
    print(f"word = {word}")
    for arg in args:
        print(arg)

say("これは固定で出す", "b", "c", "d")

