"""
Max-Min Parents and Children Algorithm
for determining the Parent-Children set
for all nodes. This returns an unoriented
graph that then must be oriented using
some set of rules or other orientation
algorithm.

Using a version of hill climbing to orient
the result of MMPC results in the MMHC -
Max-Min Hill Climbing algorithm. In other
words, MMPC can be viewed as a subroutine
of MMHC.

"""


def mmpc(data, names=None):
	nrow = data.shape[0]
	ncol = data.shape[1]
	
	if names is not None:
		names = range(ncol)
	else:
		assert(len(names)==ncol), 'names argument must be same length as data columns'

	edge_dict = dict([(n,[]) for n in names]) # rv -> children of rvs
	value_dict = dict([(n, np.unique(data[:,i])) for i,n in enumerate(names)])

	