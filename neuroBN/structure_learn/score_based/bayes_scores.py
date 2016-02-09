"""
Various Bayesian scoring metrics for evaluating
the fitness of a BN structure during score-based
structure learning.

Bayesian scoring functions:
	BD (Bayesian Dirichlet) (1995)
	BDe ("'e'" for likelihood-equivalence) (1995)
	BDeu ("'u'" for uniform joint distribution) (1991)
	K2 (1992)
"""
from __future__ import division

import numpy as np
from scipy.special import gamma, gammaln
from neuroBN.parameter_learn.mle import mle_estimator, mle_fast
from neuroBN.classes.empiricaldistribution import EmpiricalDistribution

def BDe(bn, data, ess=1, ed=None): 
	"""
	Unique Bayesian score with the property that I-equivalent
	networks have the same score.

	As Data Rows -> infinity, BDe score converges to the BIC score.

	Arguments
	---------
	*bn* : a BayesNet object
		Needed to get the parent relationships, etc.
	
	*data* : a numpy ndarray
		Needed to learn the empirical distribuion
	
	*ess* : an integer
		Equivalent sample size

	*ed* : an EmpiricalDistribution object
		Used to cache multiple lookups in structure learning.

	Notes
	-----
	*a_ijk* : a vector
		The number of times where x_i=k | parents(x_i)=j -> i.e. the mle counts

	*a_ij* : a vector summed over k's in a_ijk

	*n_ijk* : a vector prior (sample size or calculation)
		"ess" for BDe metric

	*n_ij* : a vector prior summed over k's in n_ijk
	
	"""
	counts_dict = mle_fast(bn, data, counts=True)
	a_ijk = []
	for rv, value in counts_dict.items():
		cpt = value['cpt']
		a_ijk.extend(cpt)
		a_ij.extend([sum(cpt[i:(i+bn.card(rv))]) for i in range(len(cpt)/bn.card(rv))])
		n_ijk.extend([ess]*len(cpt))
		n_ij.extend([ess*bn.card(rv)]*(len(cpt)/bn.card(rv)))

	lhs = np.prod(gamma(a_ij) / gamma(a_ij + n_ij))
	rhs = np.prod(gamma(a_ijk + n_ijk) / gamma(a_ijk))
	bde = lhs*rhs

	return bde


def BDeu(bn, data, ess=1, ed=None):
	"""
	Unique Bayesian score with the property that I-equivalent
	networks have the same score.

	As Data Rows -> infinity, BDe score converges to the BIC score.

	Arguments
	---------
	*bn* : a BayesNet object
		Needed to get the parent relationships, etc.
	
	*data* : a numpy ndarray
		Needed to learn the empirical distribuion
	
	*ess* : an integer
		Equivalent sample size

	*ed* : an EmpiricalDistribution object
		Used to cache multiple lookups in structure learning.

	Notes
	-----
	*a_ijk* : a vector
		The number of times where x_i=k | parents(x_i)=j -> i.e. the mle counts

	*a_ij* : a vector summed over k's in a_ijk

	*n_ijk* : a vector prior (sample size or calculation)
		ess/(card(x_i)*len(cpt(x_i)/card(x_i))) for x_i for BDe metric

	*n_ij* : a vector prior summed over k's in n_ijk
	
	"""
	counts_dict = mle_fast(bn, data, counts=True)
	a_ijk = []
	for rv, value in counts_dict.items():
		cpt = value['cpt']
		a_ijk.extend(cpt)
		a_ij.extend([sum(cpt[i:(i+bn.card(rv))]) for i in range(len(cpt)/bn.card(rv))])
		_ess = ess / (bn.card(rv)*(len(cpt)/bn.card(rv)))
		n_ijk.extend([_ess]*len(cpt))
		n_ij.extend([_ess*bn.card(rv)]*(len(cpt)/bn.card(rv)))

	lhs = np.prod(gamma(a_ij) / gamma(a_ij + n_ij))
	rhs = np.prod(gamma(a_ijk + n_ijk) / gamma(a_ijk))
	bde = lhs*rhs

	return bde
