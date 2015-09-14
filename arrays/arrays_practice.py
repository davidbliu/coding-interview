
def duplicate_find_left(array , left, right, value = 3):
	print 'finding'
	print str(left) + ' ' + str(right)
	if left > right:
		return -1
	if left == right and array[left] != value:
		return -1
	middle = (left + right)/2
	if value < array[middle] or (value == array[middle] and array[middle-1] == value):
		return duplicate_find_left(array, left, middle-1, value)
	if value > array[middle]:
		return duplicate_find_left(array, middle + 1, right, value)
	return middle

def duplicate_find_right(array, left, right, value = 3):
	print 'finding'
	print str(left) + ' ' + str(right)
	if left > right:
		return -1
	if left == right and array[left] != value:
		return -1
	middle = (left + right)/2
	if value < array[middle]:
		return duplicate_find_left(array, left, middle-1, value)
	if value > array[middle] or (value == array[middle] and array[middle + 1] == value):
		return duplicate_find_right(array, middle + 1, right, value)
	return middle


def surpassers(array = [2, 7, 5, 5, 2, 7, 0, 8, 1]):
	# sort the array, compare position in new array to position in old array
	print ''

def count_inversions():
	print 'counting inversions...'

def best_window(array = [-13.7, -14.5, -12.3, -12.5, -12.9], window = 1.0):
	best_start = 0
	best_end = 1
	for i in range(0, len(array)):
		while best_end < len(array) and array[best_end]-array[best_start] <= 1.0:
			print ''
def merge_intervals(intervals = [[1,3], [2,4], [5,7], [6,8]]):
	interval_stack = []
	merged_intervals = []
	for interval in intervals:
		if not interval_stack:
			interval_stack.append(interval)
		else:
			top = interval_stack[-1]
			if interval[0] < top[1]:
				interval_stack.append(interval)
			else:
				merged_intervals.append([interval_stack[0][0], interval_stack[-1][1]])
				interval_stack = [interval]
	if interval_stack:
		merged_intervals.append([interval_stack[0][0], interval_stack[-1][1]])
	return merged_intervals

if __name__ == '__main__':
	print 'hello'
	print duplicate_find_right([0,2,3,3,3,10,10], 0, 6, 3)

	listA = [0]
	listB = listA
	listB.append(1)
	listA.append(2)
	print listB
	print listA

	print 'merging intervals'
	print merge_intervals()