
def topological_sort(graph):
	stack = []
	seen = []
	base = graph.keys()
	def top_sort_helper(g, vertex):
		if vertex not in seen:
			nodes = []
			if vertex in g.keys():
				nodes = g[vertex]
			
			seen.append(vertex)
			for n in nodes:
				top_sort_helper(g, n)
			stack.append(vertex)

	for node in base:
		top_sort_helper(graph, node)


	alphabet = ''
	while len(stack) > 0:
		letter = stack.pop()
		alphabet += letter
	print alphabet
	print len(alphabet)


def get_graph():
	words = []
	with open('alien', 'r') as infile:
		words = [x.strip() for x in infile]
	print words
	graph = {}
	line_num= 0
	for i in range(0, len(words)-1):
		word1 = words[i]
		word2 = words[i+1]
		index1 = 0
		index2 = 0
		
		while index1<len(word1) and  word1[index1] == word2[index2]:
			index1+=1
			index2+=1
		if index1 != len(word1):
			line_num+=1
			mismatch = str(line_num)+': ' + word1[index1] +'->' + word2[index2]
			print mismatch
			mismatch1 = word1[index1]
			mismatch2 = word2[index2]
			if mismatch1 not in graph.keys():
				graph[mismatch1] = []
			if mismatch2 not in graph[mismatch1]:
				graph[mismatch1].append(mismatch2)

	return graph

if __name__=='__main__':

	graph = get_graph()
	print 'retrieved graph'
	print graph
	topological_sort(graph)