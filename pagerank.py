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
    for i in range(size):
        graph[i] = graph[i].split(',')
        if('-' not in graph[i]):
            graph[i] = [int(j) - 1 for j in graph[i]]

    P = np.zeros(shape=(size, size))

    for i in range(size):
        if('-' not in graph[i]):
            n = len(graph[i])
            P[i][graph[i]] = 1 / float(n)

    return csc_matrix(P,dtype=np.float)


def pagerank(P, size, error, alpha):

    e = np.ones(size) / float(size)
    r = np.ones(size) / float(size)
    ro = np.zeros(size)
    num_iter = 0

    while(np.sum(np.abs(ro-r)) > error):
        ro = r.copy()
        if(num_iter % 100):
            print('Iteration : %d Error : %0.10f' % (num_iter, np.sum(np.abs(ro-r))))

        for i in range(0, size):
            p = np.array(P[:,i].todense())[:,0]
            if(sum(p) == 0):
                p = np.ones(size) / float(size)
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
    filename = 'webgraph_test.txt'
    output = 'pagerank.txt'
    graph = readfile(filename)
    A = create_sparse_matrix(graph)
    start_time = time()
    rank = pagerank(A, len(graph), 0.0001, 0.85)
    end_time = time()
    print('Finish time : %d' % (start_time - end_time))
    writefile(rank, output)

