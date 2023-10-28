import heapq

file = open("input5.txt", "r")
file_w = open("output5.txt", "w")


def Network(Graph, source):
    Q = []
    dist = {}
    dist[source] = float('inf')
    pred = {}
    visit = [False for i in range(len(Graph) + 1)]
    for v in Graph:
        if v != source:
            dist[v] = float('-inf')
        pred[v] = None
    heapq.heappush(Q, source)
    while Q != []:
        u = heapq._heappop_max(Q)
        if visit[u]:
            continue
        visit[u] = True
        for v, next in Graph[u].items():
            a = min(dist[u], next)
            if a > dist[v]:
                dist[v] = a
                pred[v] = u
                heapq.heappush(Q, v)
                heapq._heapify_max(Q)
    for x in range(1, len(Graph)):
        if dist[x] == float('-inf'):
            dist[x] = -1
    dist[source] = 0
    lst = []
    for y in range(1, len(Graph) + 1):
        lst.append(dist[y])
    return lst


for i in range(int(file.readline())):
    s = [int(i) for i in file.readline().split(" ")]
    if s[1] == 0:
        edge = {s[0]: {}}
        source = int(file.readline())
        output = Network(edge, source)
        file_w.write(" ".join(str(elem) for elem in output)+"\n")
        continue
    edge = {}
    for j in range(s[1]):
        lst1 = [int(i) for i in file.readline().split(" ")]
        edge[(lst1[0], lst1[1])] = lst1[2]
    node = [i for i in range(1, s[0] + 1)]
    next_node = {v: {} for v in node}

    for (p, q), nxt in edge.items():
        next_node[p][q] = nxt
    source = int(file.readline())
    output = Network(next_node, source)
    file_w.write(" ".join(str(elem) for elem in output)+"\n")
