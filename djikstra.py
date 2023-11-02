import math
def djikstra (graph, start, end) :
    """
    Returns the shortest path from start to end in the given graph
    """
    # graph is a matrix that contains the distances between two places.
    # If the distance is 0, it means that the two places are not connected.
    # If the distance is non-zero, it means that the two places are connected.

    # start is the starting point
    # end is the ending point

    n = len(graph)  # number of places to visit
    init = [math.inf] * n  # init[i] is the distance from start to i
    init[start] = 0
    visited = [False] * n  # visited[i] is True if we have visited i
    current = start

    # Algorithm Implementation
    while not visited[end] and current is not None:
        for place in range(n):
            if graph[current][place] != 0 and not visited[place]:
                if init[place] > init[current] + graph[current][place]:
                    init[place] = init[current] + graph[current][place]

        visited[current] = True
        current = None
        min_dist = math.inf

        for place in range(n):
            if not visited[place] and init[place] < min_dist:
                min_dist = init[place]
                current = place

    return init[end]


