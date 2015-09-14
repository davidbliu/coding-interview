
def get_longest_path(grid):
	print 'getting longest path in grid'
	path_lengths = {}

	visited_keys = set()
	def in_bounds(i, j):
		if i < 0 or i > 3 or j < 0 or j > 3: 
			return False
		return True

	def get_longest_path_helper(i, j):
		paths = [1]

		key = i*4+j
		value = grid[i][j]
		if key in path_lengths.keys():
			return path_lengths[key]

		neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
		for neighbor in neighbors:
			x, y = neighbor[0], neighbor[1]
			if in_bounds(x, y):
				# print 'testing this neighbor ' + str(neighbor)
				if abs(grid[x][y]-grid[i][j]) == 1 and (x*4+j) not in visited_keys:
					visited_keys.add(x*4+j)
					paths.append(get_longest_path_helper(x, y) + 1)
				else:
					paths.append(1)
		# print 'got to this point'
		path_lengths[key] = max(paths) + 1
		return max(paths) + 1

	return get_longest_path_helper(0,0)

def zero_sum(array = [1,2,3,4,5,6,7,8,-1]):
	values = set()
	for elem in array:
		values.add(elem)
		if -elem in values:
			return True
	return False



if __name__ == "__main__":
	grid = [[1,2,3,4],[8,7,6,5],[2,3,4,5],[6,7,8,9]]
	longest_path = get_longest_path(grid)

	for line in grid:
		print line
	print longest_path

	# print zero_sum()