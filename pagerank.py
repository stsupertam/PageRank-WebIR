import numpy as np
from time import time
from scipy.sparse import csc_matrix


def readfile(filename):
    graph = []
    try:
        with open(filename, 'r') as file:
            graph = file.read().splitlines()
    except Exception:
        print('Cannot open file')
    return graph


def create_sparse_matrix(graph):
    size = len(graph)
    rankleak_idx = []
    for i in range(size):
        graph[i] = graph[i].split(',')
        if('-' not in graph[i]):
            graph[i] = [int(j) - 1 for j in graph[i]]

    P = np.zeros(shape=(size, size))

    for i in range(size):
        if('-' not in graph[i]):
            n = len(graph[i])
            P[i][graph[i]] = 1 / float(n)
        else:
            rankleak_idx.append(i)

    return (csc_matrix(P,dtype=np.float), rankleak_idx)


def pagerank(P, rankleak_idx, size, error, alpha):

    e = np.ones(size) / float(size)
    r = np.ones(size) / float(size)
    ro = np.zeros(size)
    num_iter = 0

    while(np.sum(np.abs(ro-r)) > error):
        print('Iteration : %d Error : %0.10f' % (num_iter, np.sum(np.abs(ro-r))))
        ro = r.copy()

        for i in range(0, size):
            p = np.array(P[:,i].todense())[:,0]
            if(i in rankleak_idx):
                p[i] = 1 / float(size)
            r[i] = ro.dot((p*alpha) + (e*(1-alpha)))
        num_iter += 1
    return r


def writefile(rank, output):
    try:
        with open(output, 'w') as file:
            for score in rank:
                file.write(str(score) + '\n')
    except Exception:
        print('Write file error')


if __name__=='__main__':
    filename = 'webgraph.txt'
    output = 'pagerank.txt'
    graph = readfile(filename)
    A, rankleak_idx = create_sparse_matrix(graph)
    start_time = time()
    rank = pagerank(A, rankleak_idx, len(graph), 0.0001, 0.85)
    end_time = time()
    print('Finish time : %d' % (end_time - start_time))
    writefile(rank, output)

