ranges = [[[i for i in range(int(range_edge.split('-')[0]),int(range_edge.split('-')[1])+1)] for range_edge in range_edges.split(',')]for range_edges in open('input.txt','r').read().splitlines()]
print(sum([1 for range in ranges if any([i in range[1] for i in range[0]]) or any([i in range[0] for i in range[1]])]))
