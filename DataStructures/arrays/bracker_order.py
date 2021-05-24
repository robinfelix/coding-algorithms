# TODO need to understand this code
def solve(s):
    p = 0
    t = 0
    res = 0
    for i in s:
        if (i == '('):
            p += 1
        else:
            p -= 1;
        print (i, t, p)
        if (p < t):
            t = p
            res = 0
        if (t == p):
            res += 1
    if p:
        return 0
    else:
        return res


s = ')()()('
print(solve(s))