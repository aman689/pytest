from typing import List
from collections import defaultdict


class Solution:

    def findTopoSort(self, node: int, vis: List[int], st: List[int],
                     adj: List[List[int]]) -> None:
        vis[node] = 1
        for it in adj[node]:
            if not vis[it[0]]:
                self.findTopoSort(it[0], vis, st, adj)
        st.append(node)

    # Function to find the shortest path from source node to all other nodes
    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        src = 0

        # Creating adjacency list from the given edges list
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))

        vis = [0] * V
        st = []

        # Finding the topological sort of the graph
        for i in range(V):
            if not vis[i]:
                self.findTopoSort(i, vis, st, adj)

        dist = [10**9] * V
        dist[src] = 0

        # Calculating the shortest path using Bellman Ford algorithm
        while st:
            node = st.pop()

            if dist[node] != 10**9:
                for it in adj[node]:
                    if dist[node] + it[1] < dist[it[0]]:
                        dist[it[0]] = dist[node] + it[1]

        # Converting unreachable nodes to -1
        for i in range(len(dist)):
            if dist[i] == 10**9:
                dist[i] = -1
        return dist
