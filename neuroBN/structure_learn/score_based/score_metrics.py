"""
Various metrics for evaluating
score-based search for Bayesian
Networks structure learning.

Generally, score-based structure learning
involves finding the structure which maximizes
some function of the likelihood of the data, given
the structure and parameters of the learned BN.

Here are a few which can be implemented:

Bayesian scoring functions:
	BD (Bayesian Dirichlet) (1995)
	BDe ("'e'" for likelihood-equivalence) (1995)
	BDeu ("'u'" for uniform joint distribution) (1991)
	K2 (1992)

Information-theoretic scoring functions:
	LL (Log-likelihood) (1912-22)
	MDL/BIC (Minimum description length/Bayesian Information Criterion) (1978)
	AIC (Akaike Information Criterion) (1974)
	NML (Normalized Minimum Likelihood) (2008)
	MIT (Mutual Information Tests) (2006)

References
----------
[1]
http://www.lx.it.pt/~asmc/pub/publications/09-TA/09-c-ta.pdf

"""
from __future__ import division


##### INFORMATION-THEORETIC SCORING FUNCTIONS #####

def log_likelihood(bn):
	"""
	Determining log-likelihood of the parameters
	of a Bayesian Network. This is a quite simple
	score/calculation, but it is useful as a straight-forward
	structure learning score.

	Semantically, this can be considered as the evaluation
	of the log-likelihood of the data, given the structure
	and parameters of the BN:
		- log( P( D | Theta_G, G ) )
		where Theta_G are the parameters and G is the structure.

	However, for computational reasons it is best to take
	advantage of the decomposability of the log-likelihood score.

	NOTE: This assumes the parameters have already
	been learned for the BN's given structure.

	LL = LL - f(N)*|B|, where f(N) = 0

	Arguments
	---------
	*bn* : a BayesNet object
		Must have both structure and parameters
		instantiated.
	"""
	return np.sum(np.log(bn.flat_cpt()))

def MDL(bn):
	"""
	Minimum Description Length score - it is
	equivalent to BIC
	"""
	return BIC(bn)

def BIC(bn):
	"""
	Bayesian Information Criterion.

	BIC = LL - f(N)*|B|, where f(N) = log(N)/2

	"""
	log_score = log_likelihood(bn)
	penalty = len(bn.flat_cpt()) / 2 * np.log(bn.num_edges())
	return log_score - penalty

def AIC(bn):
	"""
	Aikaike Information Criterion

	AIC = LL - f(N)*|B|, where f(N) = 1

	"""
	log_score = log_likelihood(bn)
	penalty = len(bn.flat_cpt())
	return log_score - penalty

















