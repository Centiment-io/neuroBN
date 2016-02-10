"""
Learn a Multi-Dimensional Bayesian Network Classifier
from data, and use it to predict a vector of class
labels from a vector of feature values.

An 'MBC' consists of two subgraphs:
	- G_c : the class subgraph,
		which includes edges only between class variables
	- G_x : the feature subgraph,
		which includes edges only between feature variables

Additionally, there is a collection of "bridge" edges:	
	- E_cx : the class-feature bridge,
		which includes the "bridge" edges between class and
		feature variables.

In an MBC, both the class sugraph and the feature subgraph can
have their own form of BN structure - e.g. empty, directed tree,
forest of trees, polytrees, or general DAGs. These 5 types of
network structures over two subgraphs means that there are 25
types of MBC structures.

To learn MBC's from data, the algorithm typically proceeds by
first learning G_c and G_x seperately using whatever structure
learning algorithm the user chooses, and then looks to optimize
the selection of "bridge" edges through further optimization
procedures.

To actually perform classification using an MBC, the traditional
Most Probable Explanation (MAP inference) procedure is employed.
The result is a vector of class predictions, which can then be
compared with the ground truth class labels to measure accuracy,
and so on.


References
----------
[1] Bielza, C., Li, G., Larranaga, P. "Multi-dimensional
classification with Bayesian networks."
[2] de Waal, P., van der Gaag, L. "Inference and Learning in
Multi-dimensional Bayesian Network Classifiers."
[3] van der Gaag, L., de Waal, P. "Multi-dimensional Bayesian
Network Classifiers."

"""

__author__ = """Nicholas Cullen <ncullen.th@dartmouth.edu>"""

def mbc(data, f_cols, c_cols, f_struct='DAG', c_struct='DAG'):
	"""

	"""
	pass





