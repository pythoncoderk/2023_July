records = [{'name': 'ALICE', 'score': 250}, {'name': 'BOB', 'score': 180}, {'name': 'CHAMP', 'score': 400}, {'name': 'DAVID', 'score': 250}]

print(type(records[0]))
print(records[0])
print(type(records))
print(records)

x = sorted(records, key=lambda e: e["score"], reverse=True)
print(x)



def ranking1(records):
    rec_sort = list(sorted(records, key=lambda r: r["score"], reverse=True))
    rank = 1
    count = 0
    last_score = None
    for r in rec_sort:
        if last_score != r["score"]:
            rank += count
            count = 0
            last_score = r["score"]
        r["rank"] = rank
        count += 1
    return rec_sort

print(ranking1(records))