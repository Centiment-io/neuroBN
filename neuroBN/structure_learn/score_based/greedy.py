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


def greedy(data, score='BIC', combined=False):
	"""
	Greedy search proceeds by choosing the move
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
	
	edge_dict = dict([(n,[]) for n in range(ncol)])

	improvement = True

	while improvement:
		pass












