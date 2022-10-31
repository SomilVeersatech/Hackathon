from math import inf


def check(g, cn, t, v, cc):
    if cn == t:
        return cc
    else:
        ls = []
        v.add(cn)
        if cn not in g.keys():
            return inf
        for ind in range(len(g[cn][0])):
            if g[cn][0][ind] in v:
                continue
            else:
                ls.append(check(g, g[cn][0][ind], t, v, cc + g[cn][1][ind]))
        if not ls:
            return inf
        else:
            return min(ls)


s = input()
g = dict()
for i in range(int(input())):
    lt = input().split()
    if lt[0] in g.keys():
        g[lt[0]][0].append(lt[1])
        g[lt[0]][1].append(int(lt[2]))
    else:
        g[lt[0]] = [[lt[1]], [int(lt[2])]]
tot_cost = 0
n = len(s)
for i in range(n // 2):
    if s[i] == s[n - 1 - i]:
        continue
    else:
        tot_cost += min(check(g, s[i], s[n - 1 - i], set(), 0), check(g, s[n - 1 - i], s[i], set(), 0))

print(tot_cost)