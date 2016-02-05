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


class EmpiricalDistribution(object):


	def __init__(self, data, names=None):
		hist,_ = np.histogramdd(data, bins=bins)
		self.joint = hist / hist.sum()

		self.NROW = data.shape[0]
		self.NVAR = data.shape[1]
		if names is None:
			self.names = range(data.shape[1])
		else:
			assert (len(names) == self.NVAR), 'Passed-in names length must equal number of data columns'
			self.names = names

		self.marginal = dict([(rv, np.sum(self.joint,axis=i)) for i,rv in enumerate(self.names)])

		self.cache = {}

	def idx_map(self, **kwargs):
		return tuple([self.names.index(kwarg) for kwarg in **kwargs])

	def jpd(self, **kwargs):
		if **kwargs not in self.cache:
			jpd = np.sum(self.joint, axis=self.idx_map(**kwargs))
			self.cache[**kwargs] = jpd
		else:
			jpd = self.cache[**kwargs]
		return jpd

	def cpd(self, x, **kwargs):
		_str = str(x) + '|' + ','.join(**Kwargs)
		if _str in self.cache:
			cpd self.cache[_str]
		else:
			tup = (x,) + **kwargs
			_numer = self.jpd(tup)
			_denom = self.jpd(**kwargs)
			cpd = _numer / (_denom + 1e-7)
		
		return cpd









