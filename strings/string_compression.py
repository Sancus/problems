import timeit

def method1(str):
    out = []
    cnt = 1
    last = str[0]
    for i, a in enumerate(str):
        if a == last and not i == len(str)-1:
            cnt = cnt+1
            continue
        out.append("%s%i" % (last, cnt))
        cnt = 1
        last = a
    final = ''.join(out)

    if len(final) < len(str):
        return ''.join(out)
    else:
        return str

print method1('aabbccaaddn')
print timeit.timeit(lambda: method1('aabbccaaddn'), number=100000)
