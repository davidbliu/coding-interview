

class MaxHeap:

	def __init__(self):
		self.heap = [0 for i in range(0, 30)]
		self.size = 0

	def insert(self, value):
		index = self.size
		self.heap[index] = value
		self.size += 1

		# bubble the value up
		parent_index = index / 2
		while parent_index != index and self.heap[parent_index] < self.heap[index]:
			temp = self.heap[parent_index]
			self.heap[parent_index] = self.heap[index]
			self.heap[index] = temp
			index = parent_index
			parent_index = index / 2


def create_max_heap(array = [1,2,3,4,5,5,6,7,9,10]):
	h = MaxHeap()
	for i in array:
		h.insert(i)
	return h

def print_heap(h):
	print [h.heap[x] for x in range(0, h.size)]

if __name__=='__main__':
	print 'hi'
	max_heap = create_max_heap()
	print_heap(max_heap)