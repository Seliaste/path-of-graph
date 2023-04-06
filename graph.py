class node():
    def __init__(self, id):
        self.id = id
        self.next = []

    def add(self, next, cost: int):
        self.next.append((next, cost))

    def nb_next(self):
        return len(self.next)

    def __len__(self):
        return self.nb_next()

    def __str__(self):
        return self.id
    __repr__ = __str__


def nb_in_graph(n: node, done: list) -> int:
    if (n not in done):
        done.append(n)
        res = 1
        for n2 in n.next:
            res += nb_in_graph(n2[0], done)
        return res
    return 0


def dijsktra(n: node):
    costs = {}
    costs[n] = 0
    noir = []
    gris = [node[0] for node in n.next]
    for node in n.next:
        costs[node[0]] = node[1]
    while len(gris) != 0:
        curr = min(gris, key=costs.get)
        for node in curr.next:
            val = costs[curr]+node[1]
            if (node in noir and val < costs[node]) or node not in noir:
                costs[node[0]] = val
        noir.append(curr)
        gris.remove(curr)
    return costs


a = node("A")
b = node("B")
c = node("C")
d = node("D")
e = node("E")

a.add(d, 2)
a.add(e, 3)
b.add(a, 11)
c.add(e, 8)
c.add(a, 1)
d.add(c, 5)
e.add(b, 7)

print(dijsktra(a))
