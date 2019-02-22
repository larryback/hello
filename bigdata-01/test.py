def add_commas(s, widths):
    ss = iter(s)
    for w in widths:
        for _ in range(w):
            try:
                yield next(ss)
            except StopIteration:
                return
        yield ","
    yield from ss

print(''.join(add_commas("this is really long", [4, 3, 5])))
# 'this, is, real,ly long'