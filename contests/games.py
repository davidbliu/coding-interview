
def solve_sieve():
	total = sum([x for x in range(2, 1000000)] )
	two = sum([x for x in range(2, 1000000) if x%2 ==0 or x%3==0 or x%5==0 or x%7==0])
	print total-two

def solve_aliens():
	alphabet = {}
	seen_letters = set()
	with open('alien2', 'r') as infile:
		words = []
		for i in infile:
			i= i.replace(' ', '').replace('\n', '')
			words.append(i)
	print words

def solve_sushi():
	pass

import math
import numpy as np 
def solve_ship():
	coords = []
	with open('ships', 'r') as infile:
		for i in infile:
			coord = i.replace('\n', '').split(' ')
			coord = [float(x) for x in coord]
			coords.append(coord)

	def distance(ship1, ship2):
		return np.linalg.norm(np.asarray(ship1)-np.asarray(ship2))

	best_connected = 0
	connectivity = []
	seen = set()
	for i in range(0, len(coords)):
		print i
		if i not in seen:
			connected = [j for j in range(0, len(coords)) if distance(coords[j], coords[i]) < 100]
			connectivity.append(set(connected))
			seen = seen.union(set(connected))
	connectivity = [i for i in connectivity if len(i)>0]
	
	for con in connectivity:
		for other in connectivity:
			if len(other.intersection(con))!=0:
				con = con.union(other)
	print connectivity

	maxlen = 0
	for con  in connectivity:
		leng = len(con)
		if leng>maxlen:
			maxlen = leng
	return maxlen


# print solve_ship()
import random

def solve_dice():
	def simulate(final_score = 30, numtrials = 10000):
		results = []
		for _ in range(numtrials):
			score = 0
			rolls = 0
			while score < final_score:
				rolls+=1
				die = random.randint(1,6)
				if die == 1:
					score = 0
				else: 
					score+=die

			results.append(rolls)
		print sum(results)/float(len(results))
		return results

	def calculate_expected(final_score):
		scores = {}
		for i in range(7):
			scores [-i] = 0
		scores[1] = 1.2
		scores[2] = 1.2
		# scores[3] = 
		p = 1/float(6)
		for i in range(0, final_score+1):
			scores[i] = 6/float(5) * (p + p*sum([scores[i-x]+1 for x in [2,3,4,5,6]]))
		for i in scores.keys():
			print 'E(X = ' + str(i)+') = '+str(scores[i])
	for i in range(30):
		print 'simulating '+str(i)
		simulate(final_score = i)

solve_dice()




