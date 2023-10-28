"""
As there is different traffic level in this graph, we can consider it as a weighted graph.
We all know that BFS only works for unweighted graph. That's why here, in this problem,
we cannot use the BFS algorithm rather we have to use the Dijkstra algorithm to find out the shortest path.
"""


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[0 for j in range(v)] for k in range(v)]

    def minDist(self, distance, sp):
        min_dist = 1e10
        for v in range(self.v):
            if distance[v] < min_dist and sp[v] == False:
                min_dist = distance[v]
                result = v
        return result

    def dijkstra(self, s):
        distance = [1e10] * self.v
        distance[s] = 0
        sp = [False] * self.v
        for count in range(self.v):
            u = self.minDist(distance, sp)
            sp[u] = True
            for v in range(self.v):
                if int(self.graph[u][v]) > 0 and (sp[v]) == False:
                    if (distance[v]) > (distance[u]) + int(self.graph[u][v]):
                        (distance[v]) = (distance[u]) + int(self.graph[u][v])

        return distance


file = open("input1.txt", "r")
file_w = open("output1.txt", "w")
total_edge = len(file.readlines())
# print('Total lines:', total_edge)
file.close()
file = open("input1.txt", "r")
src = []
dst = []
val = []
start = input("Starting place? ")
end = input("Destination? ")
for i in range(total_edge):
    x, y, z = file.readline().strip().split(" ")
    src.append(x)
    dst.append(y)
    val.append(z)
temp_vtx = list(set(src + dst))
a = temp_vtx.remove(start)
b = temp_vtx.remove(end)
temp_vtx.sort()
all_vtx = [start]
for i in temp_vtx:
    all_vtx.append(i)
all_vtx.append(end)

# print("*", all_vtx, "\n", src, "\n", dst, "\n", val)
all_vtx_dict = dict(zip(all_vtx, range(len(all_vtx))))
# print(all_vtx_dict)
g = Graph(len(all_vtx))
for i, tl in enumerate(val):
    g.graph[all_vtx_dict[src[i]]][all_vtx_dict[dst[i]]] = tl
    g.graph[all_vtx_dict[dst[i]]][all_vtx_dict[src[i]]] = tl
dist = g.dijkstra(0)
a = dist[len(all_vtx) - 1]
print("Shortest distance from " + start + " to " + end + " using Dijkstra Algorithm is:", dist[len(all_vtx) - 1])
file_w.write("Shortest distance from " + start + " to " + end + " using Dijkstra Algorithm is: " + str(a))
