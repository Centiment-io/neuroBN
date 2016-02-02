# Bayesian Networks for Neuroscience

<h2>Overview</h2>
Many research fields have benefit from the flexibility and expressiveness of the Bayesian Network framework - medicine, economics, artificial intelligence, social science, and many more. Still, Bayesian networks have failed to penetrate the field of neuroscience, where they could be of incredible use. With that in mind, this project is aimed at making Bayesian Networks more accessible to neuroscientists. The motivation for this project is very much derived from the review paper by Bielza and Larranaga - "Bayesian networks in neuroscience: a survey."

As it relates to neuroscience, this code base aims to perform the following general tasks:
- <b><i>Function Connectivity Mapping</i></b>
	- looking for network-based relationships among variables of interest. This is
known in the more general case as "Association Discovery".
- <b><i>Feature Selection</i></b> 
	- choosing the appropriate features (variables) to use in classifying a target variable, or otherwise
reducing the dimensionality of a large dataset.
- <b><i>Supervised Classification</i></b>
	- predict class labels of new data from training data.
- <b><i>Unsupervised Classification</i></b>
	- learning from data where the ground truth is unknown. One example of this task is "clustering" - assigning data into clusters of similar observations.
- <b><i>Inference</i></b>
	- answering marginal or conditional probability queries, such as "what is the probability a person will develop dimentia given that he/she is 60 years old and had a stroke within the last five years?"

<h2>Data</h2>

The goal is to achieve full availability of state-of-the-art Bayesian network functionality for seamless use with all types of neuroscience data.
- Morphological Data
- Electrophysiological Data
- Genomics/Proteomics/Transcriptomics Data
- Neuroimaging Data
	- fMRI
	- MRI
	- EEG
- Others
	- ECoG, EMG, JME, TCD, DTI, PET

<h2>Call for Researchers</h2>
If you are a neuroscience researcher or student who thinks the incredible learning/classification/inference functionality of Bayesian networks can add value to your work or want to see support for a specific type of data, please contact me and I will either a) answer questions or give advice on how to get the most out of neuroBN or b) work with you to build custom functionality that integrates your work with the neuroBN code. Email me at ncullen.th@dartmouth.edu.




<h2>Survey of Existing Literature</h2>
Below is a set of tables highlighting the use of Bayesian networks in the existing neuroscience literature. Please note that these tables are adapted directly from <i>Bielza, C., and Larranaga, P. "Bayesian networks in neuroscience: a survey"</i> ([1]) -- permitted under the Creative Commons License. Absolutely all credit for the following tables belongs to those two researchers.
<h4>BNs with Morphological Data</h4>

| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| DeFelipe et al., 2013 | BN and naive Bayes | Assoc. and supervised class | Classification and naming of GABAergic interneurons |
| Lopez-Cruz et al., 2014 | BN and BN multinet | Assoc. and inference and cluster | Consensus model for interneuron classification |
|Mihaljevic et al., in press | Naive Bayes and TAN | Supervised class | Classification of cortical GABAergic interneurons |
|Mihaljevic et al., Under review | MBC | Multi-dimensional class | Simultaneous classification of six axonal class variables |
|Guerra et al., 2011 | Naive Bayes | Supervised class | Pyramidal neuron vs. interneuron |
|Lopez-Cruz et al., 2011 | BN | Inference, associations | Model and simulation of dendritic trees |

<h4>BNs with Electrophysical Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Smith et al., 2006 | Dynamic BN | Association | Infer non-linear neural information flow networks |
| Eldawlatly et al., 2010 | Dynamic BN | Association | Infer effective and time-varying connectivity between spiking cortical neurons |
| Jung et al., 2010 | BN | Association | Neuronal synchrony from electrode signal recordings |
| Pecevski et al., 2011 | BN | Inference | Emulate probabilistic inference through networks of spiking neurons |

<h4>BNs with 'Omics Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Armañanzas et al., 2012 | Ensemble of BN classifiers | Association | Transcripts in AD |
| Hullam et al., 2012 | BN | Association | SNPs in depression |
| Zeng et al., 2013 | BN | Association | Cytokines and mRNA in cerebral ischemia |
| Liang et al., 2007 | BN | Association | SNPs in childhood absence epilepsy |
| Zhang et al., 2010 | BN | Association | Regulation network of the neuron-specific factor Nova (mice) |
| Jiang et al., 2011 | BN | Association | SNPs in late onset AD |
| Han et al., 2012 | BN | Association | SNPs in early onset autism |
| Wei et al., 2011 | Model-averaged naive Bayes, selective naive Bayes |Sup. classification | Prediction of AD from SNPs |
| Gollapalli et al., 2012 | Selective naive Bayes | Sup. classification | Mass spectrometry for predicting glioblastoma |
| Belgard et al., 2011 | Naive Bayes | Sup. classification | Distinguish sequenced transcriptomes among layers I-VIb |



<h2>References</h2>
- [1] Bielza, C., Larranaga, P. "Bayesian networks in neuroscience: a survey"
- [2] Daly, R., Shen, Q., Aitken, S. "Learning Bayesian networks: approaches and issues"
- [3] Bielza, C., Li, G., Larranaga, P. "Multi-dimensional classification with Bayesian networks"
- [4] Pham, D., Ruz, G. "Unsupervised training of Bayesian networks for data clustering"








