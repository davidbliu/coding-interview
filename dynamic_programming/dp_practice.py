import sys
# you can subtract 1, divide 3, divide 2
def steps_to_one(n = 7):
	steps = {}
	steps[1] = 1
	steps[2] = 1
	steps[3] = 1
	for i in range(4, n+1):
		steps[i] = min(steps[i-1], steps[i/2] if i%2==0 else sys.maxint, steps[i/3] if i%3==0 else sys.maxint) + 1
		print str(i) + ': ' + str(steps[i])

	return steps[n]

def longest_increasing_subsequence(array = None):
	print 'calculating longest increasing subsequence...'

def knapsack():
	print 'solving knapsack...'




def house_coloring():
	print 'house coloring (linkedin fall 2014)'
if __name__=='__main__':
	print 'hi'
	print steps_to_one()