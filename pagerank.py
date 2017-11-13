import numpy as np
from scipy.sparse import csc_matrix

with open('webgraph_test.txt', 'r') as file:
    graph = file.read().splitlines()

size = len(graph)
for i in range(size):
    graph[i] = graph[i].split(',')
    if('-' not in graph[i]):
        graph[i] = [int(j) - 1 for j in graph[i]]

P = np.zeros(shape=(size, size))

for i in range(size):
    if('-' not in graph[i]):
        n = len(graph[i])
        P[i][graph[i]] = 1 / float(n)

P = csc_matrix(P,dtype=np.float)
error = 0.0001
alpha = 0.85

num_iter = 0
r = np.ones(size) / float(size)
ro = np.zeros(size)

e = np.ones(size) / float(size)

while(np.sum(np.abs(ro-r)) > error):
    ro = r.copy()
    print('Iteration : %d' % (num_iter + 1))
    for i in range(0, size):
        p = np.array(P[:,i].todense())[:,0]
        if(sum(p) == 0):
            p = np.ones(size) / float(size)
        r[i] = ro.dot((p*alpha) + (e*(1-alpha)))
    num_iter += 1

with open('pagerank.txt', 'w') as file:
    for score in r:
        file.write(str(score) + '\n')