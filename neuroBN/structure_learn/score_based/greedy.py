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
"""

from scipy.optimize import *
import numpy as np

from neuroBN.parameter_learn.mle import mle_estimator
from neuroBN.parameter_learn.bayes import bayes_estimator
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
	if names is None:
		names = range(ncol)

	# INITIALIZE BAYESIAN NETWORK W/ NO EDGES
	edge_dict = dict([(n,[]) for n in names])
	value_dict = dict([(n, np.unique(data[:,i])) for i,n in enumerate(names)])
	bn = BayesNet(edge_dict, value_dict)

	# COMPUTE INITIAL LIKELIHOOD SCORE
	max_score = structure_score(bn, data, metric)

	#nodes = range(ncol)

	
	max_score = -1e7
	_iter = 0
	improvement = True

	while improvement:
		improvement = False
		temp_max = max_score

		# Test Arc Additions
		# bn.add_edge(u,v)
		for u in bn.nodes():
			for v in bn.nodes():
				if not would_cause_cycle(bn, u, v):
					# THIS ONLY WORKS IF mle_estimator
					# DOESNT ALTER BN DATA DIRECTLY... fix that.
					old_cpt = bn.cpt(v)
					bn.add_edge(u, v)
					mle_estimator(bn, data, v)
					new_cpt = bn.cpt(v)
					score_difference = None

		# Test Arc Deletions
		# bn.remove_edge(u,v)

		# Test Edge Reversals
		# bn.reverse_edge(u,v)

		if temp_max != max_score:
			improvement = True
		
		if _iter > MAX_ITER:
			break

	return bn
















