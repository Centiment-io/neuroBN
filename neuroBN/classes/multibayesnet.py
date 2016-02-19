"""
*****************
Multi-Dimensional 
Bayesian Network
*****************

This is the class for a multi-dimensional BN, which
is mostly used for multi-label classification. It
inherits from the BayesNet class.

"""
__author__ = """Nicholas Cullen <ncullen.th@dartmouth.edu>"""

from neuroBN.classes.bayesnet import BayesNet

class multiBayesNet(BayesNet):

	def __init__(self, partition=None):
		"""
		Constructor for multiBayesNet class.

		Arguments
		---------
		*partition* : a list with N sublists
			Each sublist should contain the variable names
			(i.e. strings) which belong to that partition.

			Regardless of the number of sublists, the
			target variable partition should be the first
			sublist.

			Note that the traditional multiBayesNet
			should be a list with exactly 2 sublists.

		"""
		super(multiBayesNet, self).__init__()		
		self.partition = partition