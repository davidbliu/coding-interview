class ListNode:
	def __init__(self, val):
		self.value = val
		self.next = None




def construct_list():
	node = ListNode(0)
	curr = node
	for i in range(1, 10):
		next = ListNode(i)
		curr.next = next
		curr = curr.next
	return node

def print_list(node):
	print 'printing list'
	curr = node
	while curr != None:
		print curr.value
		curr = curr.next

def reverse_list(node):
	print 'reversing list...'
	prev = node
	curr = node
	next = node.next
	while curr != None:
		next = next.next
		curr.next = prev
		prev = curr
		curr = next
		# print curr.value
		# print str(next.value) + ' ' + str(curr.value) + ' ' + str(prev.value)
	return prev

if __name__=='__main__':
	print 'reversing singly linked ListNode'
	n = construct_list()
	print_list(n)
	r = reverse_list(n)
	print 'done'
	print_list(r)
