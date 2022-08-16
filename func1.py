def modify_list(l):
    i, n = 0, len(l)
    while i < n:
        if l[i] % 2:
            l.pop(i)
            n -= 1
        else:
            l[i] = l[i] // 2
            i += 1