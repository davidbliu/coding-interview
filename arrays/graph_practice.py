import Queue

g={1: [2, 3,6], 2: [4, 5], 3: [6, 7],4:[8,9,13]}

def bfs_levels(graph):
	keys = graph.keys()
	search_queue = Queue.Queue()
	for key in keys:
		search_queue.put(key)
	visited = set()
	level_queue = Queue.Queue()
	while not search_queue.empty():
		curr = search_queue.get()
		if curr not in visited:
			print curr
		visited.add(curr)
		if curr in graph.keys():
			childs = graph[curr]
			for node in childs:
				if node not in visited:
					level_queue.put(node)
		if search_queue.empty():
			search_queue = level_queue
			level_queue = Queue.Queue()
			print '***'


	print 'hi'

# return minimum spanning tree (set of edges)
def mst():
	pass

bfs_levels(g)