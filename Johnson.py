"""
1. Run Bellman-Ford ensures no negative-weight cycle
2. Add one source s to all vertices with path length 0
3. Run Bellman-Ford to compute shortest path from s to all vertices
4. Now do weight re-weighting to eliminate negative weight
    a. w' = w - wu(head) + wv(tail)
5. Now all weight is non-negative. Do Dijkstra for all pairs shortest path
6. If implement min-priority queue in Dijkstra by a Fibonacci heap, Johnson
    algorithm run O(V^2 lgV + VE)
"""
def Johnson(G,w):
    pass