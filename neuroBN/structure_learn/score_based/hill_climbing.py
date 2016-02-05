"""
Code for Searching through the space of
possible Bayesian Network structures.

Various optimization procedures are employed,
from greedy search to simulated annealing, and 
so on - mostly using scipy.optimize.

Local search - possible moves:
- Add edge
- Delete edge
- Invert edge

Strategies to improve Greedy Hill-Climbing:
- Random Restarts
	- when we get stuck, take some number of
	random steps and then start climbing again.
- Tabu List
	- keep a list of the K steps most recently taken,
	and say that the search cannt reverse (undo) any
	of these steps.
"""

from scipy.optimize import *
import numpy as np
from heapq import *

from neuroBN.classes.bayesnet import BayesNet
from neuroBN.parameter_learn.mle import mle_estimator
from neuroBN.structure_learn.score_based.scores import structure_score
from neuroBN.utils.independence_tests import mutual_information
from neuroBN.utils.graph import would_cause_cycle


def hill_climbing(data, metric='AIC', MAX_ITER=5):
	"""
	Greedy Hill Climbing search proceeds by choosing the move
	which maximizes the increase in fitness of the
	network at the current step. It continues until
	it reaches a point where there does not exist any
	feasible single move that increases the network fitness.

	It is called "greedy" because it simply does what is
	best at the current iteration only, and thus does not
	look ahead to what may be better later on in the search.

	For computational saving, a Priority Queue (python's heapq) 
	can be used	to maintain the best operators and reduce the
	complexity of picking the best operator from O(n^2) to O(nlogn).
	This works by maintaining the heapq of operators sorted by their
	delta score, and each time a move is made, we only have to recompute
	the O(n) delta-scores which were affected by the move. The rest of
	the operator delta-scores are not affected.

	For additional computational efficiency, we can cache the
	sufficient statistics for various families of distributions - 
	therefore, computing the mutual information for a given family
	only needs to happen once.

	The possible moves are the following:
		- add edge
		- delete edge
		- invert edge

	Arguments
	---------
	*data* : a nested numpy array
		The data from which the Bayesian network
		structure will be learned.

	*score* : a string
		Which score metric to use.
		Options:
			- AIC
			- BIC / MDL
			- LL (log-likelihood)
	"""
	nrow = data.shape[0]
	ncol = data.shape[1]
	
	names = range(ncol)

	# INITIALIZE NETWORK W/ NO EDGES
	# maintain children and parents dict for fast lookups
	c_dict = dict([(n,[]) for n in names])
	p_dict = dict([(n,[]) for n in names])
	
	# COMPUTE INITIAL LIKELIHOOD SCORE	
	value_dict = dict([(n, np.unique(data[:,i])) for i,n in enumerate(names)])
	bn = BayesNet(c_dict)
	mle_estimator(bn, data)
	max_score = structure_score(bn, nrow, metric)

	# CREATE EMPIRICAL DISTRIBUTION OBJECT FOR CACHING
	#ED = EmpiricalDistribution(data,names)

	

	_iter = 0
	improvement = True

	while improvement:
		improvement = False
		max_delta = 0

		### Test Arc Additions ###
		# ONE FAMILY AFFECTED BY ARC ADDITION
		for u in bn.nodes():
			for v in bn.nodes():
				if v not in c_dict[u] and not would_cause_cycle(c_dict, u, v):
					old_cols = (u,) + tuple(p_dict[u])
					mi_old = mutual_information(data[:,old_cols])
					new_cols = old_cols + (v,)
					mi_new = mutual_information(data[:,new_cols])
					delta_score = nrow * (mi_old - mi_new)

					if delta_score > max_delta:
						print 'Improvement: ' , (u,v) , '\n'
						print 'Delta Score: ' , delta_score , '\n'
						max_delta = delta_score
						max_operation = 'Addition'
						max_arc = (u,v)


		# DETERMINE IF/WHERE IMPROVEMENT WAS MADE
		if max_delta != 0:
			improvement = True
			print 'Adding: ' , max_arc
			u,v = max_arc
			if max_operation == 'Addition':
				c_dict[u].append(v)
				p_dict[v].append(u)
		else:
			print 'No Improvement on Iter: ' , _iter

		
		_iter += 1
		if _iter > MAX_ITER:
			print 'Max Iteration Reached'
			break

	
	bn = BayesNet(c_dict, value_dict)

	return bn
















