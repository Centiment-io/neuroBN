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
import numpy as np
from scipy.special import gamma, gammaln
from neuroBN.parameter_lean.mle import mle_estimator


def BDe(bn, data, ess): 
	"""
	Unique Bayesian score with the property that I-equivalent
	networks have the same score.

	As Data Rows -> infinity, BDe score converges to the BIC score.


	NOTES
	-----
	r_i : the cardinality of variable i ==> bn.card(rv)
	q_i : product of cardinalities of i's parents ==> len(bn.cpt(rv))/bn.card(rv)
	Theta_ijk = fraction of instances for variable i where r_i=k and q_i=j
	Theta_ij = sum of Theta_ijk over all states r_i of variable i where q_i=j
	N_ijk = the number of cases in the data where x_i=k and q_i=j
	N_ij = sum of N_ijk over all states r_i of variable i where q_i=j in the data

	alpha : equivalent sample size
	alpha(x, pa(x)) = alpha*P(x,pa(x))
	"""
	cont_table = mle_estimator(bn, data, counts=True)

	flat_cpt = equiv_sample*bn.flat_cpt()
	flat_var_cpt = equiv_sample*bn.flat_cpt(by_parents=True)

	bde = np.prod(gamma(flat_cpt) / (gamma(flat_cpt+1))) * np.prod(gamma(flat_cpt+1)/gamma(flat_cpt))
	return bde


def BDeu(bn):
	"""
	Uniform prior on the structure.
	"""
	pass

def K2(bn):
	pass