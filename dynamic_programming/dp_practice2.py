# int [] B = {-15, 29, -36, 3, -22, 11, 19, -5};
# http://karmaandcoding.blogspot.com/2012/02/dynamic-programming-maximum-value.html
def max_contiguous_subsequence(array = [-15,29,-36, 3, -22, 11, 19, -5]):
	print 'solving...'
	print max_subarray(array)

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# longest increasing subsequence
def longest_increasing_subsequence(A=[5,3,4,7,3,23,5,5,6,7,8,9]):
	print 'solving...'
# making change 
# You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all i
#ntegers). Assume v(1) = 1, so you can always make change for any amount of money C. 
#Give an algorithm which makes change for an amount of money C with as few coins as possible.
if __name__=='__main__':
	max_contiguous_subsequence()