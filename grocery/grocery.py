g = dict()
try:
    while True:
        item = input().strip().upper()
        g[item] = g.get(item,0) + 1

except EOFError:
    sort = sorted(g.keys())
    for _ in sort:
        print(f"{g.get(_)} {_}")