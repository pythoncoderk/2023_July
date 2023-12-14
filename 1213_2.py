l = [2, 5, 1, 4, 6, 3, 9, 15]
def original_sort(lists):
    l2 = []
    for i in range(len(lists)):
        lists_count = lists[:]
        x = min(lists_count)
        l2.append(x)
        l.pop(l.index(x))
    return print(l2)

original_sort(l)