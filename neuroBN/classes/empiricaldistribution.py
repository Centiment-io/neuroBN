"""
************
Empirical
Distribution
Class
************

Create, maintain, and perform operations
over an empirical probability distribution
derived from a dataset.
"""

from __future__ import division

import numpy as np


class EmpiricalDistribution(object):


	def __init__(self, data, names=None):

		if names is None:
			self.names = range(data.shape[1])
		else:
			assert (len(names) == self.NVAR), 'Passed-in names length must equal number of data columns'
			self.names = names

		self.NROW = data.shape[0]
		self.NVAR = data.shape[1]
		self.bins = [len(np.unique(data[:,n])) for n in range(self.NVAR)]
		

		hist,_ = np.histogramdd(data, bins=self.bins)
		self.joint = (hist / hist.sum()) + 1e-3

		## COMPUTE MARGINAL FOR EACH VARIABLE ##
		_range = range(self.NVAR)
		for i,rv in enumerate(self.names()):
			_axis = copy(_range)
			_axis.remove(i)
			self.marginal[rv] = np.sum(self.joint,axis=_axis)

		self.marginal = dict([(rv, np.sum(self.joint,axis=i)) for i,rv in enumerate(self.names)])

		self.cache = {}

	def idx_map(self, rvs):
		assert (isinstance(args, tuple)), "passed-in rvs must be a tuple"
		idx = [self.names.index(rv) for rv in rvs]
		return tuple(idx)

	def idx(self, rv):
		return self.names.index(rv)

	def axis_tuple(self, rv):
		pass

	def mpd(self, rv):
		"""
		Marginal Probability Distribtuion
		"""
		assert (isinstance(rv, str)), 'passed-in rv must be a string'
		if rv in self.cache:
			mpd = self.cache[rv]
		else:
			_axis = range(self.NVAR)
			_axis.remove(self.idx(rv))
			mpd = np.sum(self.join, axis=tuple(_axis)) # CORRECT
			self.cache[rv] = mpd

		return mpd

	def jpd(self, rvs):
		assert (isinstance(args, tuple)), "passed-in rvs must be a tuple"
		if args in self.cache:
			jpd = self.cache[rvs]
		else:
			jpd = np.sum(self.joint, axis=self.idx_map(rvs)) # WRONG 
			self.cache[rvs] = jpd
			
		return jpd

	def cpd(self, lhs, rhs):
		assert (isinstance(rhs, tuple)), "passed-in rhs must be a tuple"

		_key = tuple((lhs,rhs))
		if _key in self.cache:
			cpd = self.cache[_key]
		else:
			try:
				tot = lhs + rhs
			except TypeError:
				tot = (lhs,) + rhs

			_numer = self.jpd(tot)
			_denom = self.jpd(rhs)
			cpd = _numer / (_denom + 1e-7)
			self.cache[_key] = cpd
		
		return cpd









