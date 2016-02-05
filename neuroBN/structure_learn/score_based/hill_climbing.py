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

from neuroBN.utils.independence_tests import mutual_information
from neuroBN.utils.graph import would_cause_cycle


def hill_climbing(data, metric='BIC', MAX_ITER=1000):
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
	NROW = data.shape[0]
	ncol = data.shape[1]
	if names is None:
		names = range(ncol)

	# INITIALIZE NETWORK W/ NO EDGES
	# maintain children and parents dict for fast lookups
	c_dict = dict([(n,[]) for n in names])
	p_dict = dict([(n,[]) for n in names])
	
	# COMPUTE INITIAL LIKELIHOOD SCORE	
	value_dict = dict([(n, np.unique(data[:,i])) for i,n in enumerate(names)])
	bn = BayesNet(c_dict, value_dict)
	mle_estimator(bn, data)
	max_score = structure_score(bn, data, metric)

	# CREATE EMPIRICAL DISTRIBUTION OBJECT FOR CACHING
	ED = EmpiricalDistribution(data,names)

	

	_iter = 0
	improvement = True

	while improvement:
		improvement = False
		max_delta = 0

		### Test Arc Additions ###
		# ONE FAMILY AFFECTED BY ARC ADDITION
		for u in bn.nodes():
			for v in bn.nodes():
				if not would_cause_cycle(bn, u, v):
					old_cols = (u,) + tuple(p_dict[u])
					mi_old = mutual_information(data[:,old_cols])
					new_cols = old_cols + (v,)
					mi_new = mutual_information(data[:,new_cols])
					penalty_new = np.log(1) / 2 * added_params
					delta_score = NROW * (mi_old - mi_new - penalty_new)

					if delta_score > max_delta:
						max_delta = delta_score
						max_operation = 'Addition'
						max_arc = (u,v)

		### Test Arc Deletions ###
		# ONE FAMILY AFFECTED BY ARC DELETION
		for u in bn.nodes():
			for v in bn.nodes():
				if not would_cause_cycle(bn, u, v):
					#old_cols = 
					mi_old = mutual_information(data[:,old_cols])
					mi_new = mutual_inforamtion(data[:,new_cols])
					penalty_new = np.log(1) / 2 * added_params
					delta_score = NROW * (mi_old - mi_new - penalty_new)

					if delta > max_delta:
						max_delta = delta
						max_operation = 'Deletion'
						max_arc = (u,v)

		### Test Edge Reversals ###
		# TWO FAMILIES ARE AFFECTED BY ARC REVERSAL
		for u in bn.nodes():
			for v in bn.nodes():
				if not would_cause_cycle(bn, u, v):
					#old_cols = 
					mi_old = mutual_information(data[:,old_cols])
					mi_new = mutual_inforamtion(data[:,new_cols])
					penalty_new = np.log(1) / 2 * added_params

					diff = NROW * (mi_old - mi_new - penalty_new)

					if diff > max_diff:
						max_diff = diff
						max_operation = 'Reversal'
						max_arc = (u, v)

		# DETERMINE IF/WHERE IMPROVEMENT WAS MADE
		if max_diff != 0:
			improvement = True
			u,v = max_arc
			if max_operation == 'Addition':
				c_dict[u].append(v)
				p_dict[v].append(u)
				#bn.add_edge(u,v)
			elif max_operation == 'Deletion':
				c_dict[u].remove(v)
				p_dict[v].remove(u)
				bn.remove_edge(u,v)
			elif max_operation == 'Reversal':
				c_dict[u].remove(v)
				c_dict[v].append(u)
				p_dict[v].remove(u)
				p_dict[v].append(u)
				#bn.reverse_edge(u, v)
			
			# RECOMPUTE SUFFICIENT STATISTICS ?
			#mle_estimator(bn, data, v)
		
		_iter += 1
		if _iter > MAX_ITER:
			break

	value_dict = dict([(n, np.unique(data[:,i])) for i,n in enumerate(names)])
	bn = BayesNet(c_dict, value_dict)

	return bn
















