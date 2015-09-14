# given a directed graph, find whether there is a route between two nodes

""" dijstras algorithm """
import Queue
from collections import deque
Dictionary = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']

def is_connected(word1, word2):
		differences = 0
		if len(word1) != len(word2):
			return false
		for i in range(0, len(word1)):
			if word1[i] != word2[i]:
				differences += 1
		return differences == 1

def shortest_chain(words, word, target):
	explore = deque([[x] for x in words if is_connected(word, x)])
	visited = [x[0] for x in explore]
	while explore:
		w = explore.popleft()
		lastword = w[-1]
		nextwords = [x for x in words if x not in visited and is_connected(lastword, x)]
		for nextword in nextwords:
			if nextword == target:
				return ([word]+w+[nextword])
			visited.append(nextword)
			explore.append(w + [nextword])



print is_connected('POON', 'SAME')
print shortest_chain(Dictionary, 'TOON', 'PLEA')

