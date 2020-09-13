#Uses python3

import sys
import queue

def bipartite(adj, n):
    partition = [(None) for _ in range(n)]
    q = queue.Queue()
    q.put(0)
    partition[0] = 'Black'
    while not q.empty():
        x = q.get()
        for i in adj[x]:
            if partition[i] == partition[x]:
                return 0
            elif partition[i] is None:
                q.put(i)
                if partition[x] == 'Black':
                    partition[i] = 'White'
                else:
                    partition[i] = 'Black'
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj, n))