# Bayesian Networks for Neuroscience

<h2>Overview</h2>
Many research fields have benefit from the flexibility and expressiveness of the Bayesian Network framework - medicine, economics, artificial intelligence, social science, and many more. Still, Bayesian networks have failed to penetrate the field of neuroscience, where they could be of incredible use. With that in mind, this project is aimed at making Bayesian Networks more accessible to neuroscientists. The motivation for this project is very much derived from the review paper by Bielza and Larranaga - "Bayesian networks in neuroscience: a survey."

As it relates to neuroscience, this code base aims to perform the following general tasks:
- Function Connectivity Mapping : looking for network-based relationships among variables of interest. This is
known in the more general case as "Association Discovery".
- Feature Selection : choosing the appropriate features (variables) to use in classifying a target variable, or otherwise
reducing the dimensionality of a large dataset.
- Supervised Classification : predict class labels of new data from training data.
- Unsupervised Classification : learning from data where the ground truth is unknown. One example of this task is "clustering" - assigning data into clusters of similar observations.

<h2>Data</h2>

The goal is to achieve full availability of state-of-the-art Bayesian network functionality for seamless use with all types of neuroscience data:
- Morphological Data
- Electrophysiological Data
- Genomics/Proteomics/Transcriptomics Data
- Neuroimaging Data
	- fMRI
	- MRI
	- EEG
- Others
	- ECoG
	- EMG
	- JME
	- TCD
	- DTI
	- PET

<h2>Call for Researchers</h2>
If you are a neuroscience researcher or student who thinks the incredible learning/classification/inference functionality of Bayesian networks can add value to your work, please contact me and I will either a) answer questions or give advice on how to get the most out of neuroBN or b) work with you to build custom functionality that integrates your work with the neuroBN code. Email me at ncullen.th@dartmouth.edu.


<h2>References</h2>
- [1] Bielza, C., Larranaga, P. "Bayesian networks in neuroscience: a survey"
- [2] Daly, R., Shen, Q., Aitken, S. "Learning Bayesian networks: approaches and issues"
- [3] Bielza, C., Li, G., Larranaga, P. "Multi-dimensional classification with Bayesian networks"
- [4] Pham, D., Ruz, G. "Unsupervised training of Bayesian networks for data clustering"