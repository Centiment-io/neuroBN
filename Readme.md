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
| Wei et al., 2011 | Model-averaged NB, selective NB |Sup. classification | Prediction of AD from SNPs |
| Gollapalli et al., 2012 | Selective NB | Sup. classification | Mass spectrometry for predicting glioblastoma |
| Belgard et al., 2011 | Naive Bayes | Sup. classification | Distinguish sequenced transcriptomes among layers I-VIb |

<h4>BNs with fMRI Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Iyer et al., 2013 | Gaussian BNs | Association | Resting-state (normal subjects)| 
| Dawson et al., 2013 | Gaussian BNs | Association | Resting-state (normal subjects)| 
| Li et al., 2011 | Gaussian BNs | Association | Resting-state (normal subjects)| 
| Li et al., 2013 | Gaussian BNs | Association | Resting-state (aMCI vs. controls)| 
Labatut et al., 2004 | Gaussian dynamic BNs | Association | Phoneme task (normal vs. dyslexic) | 
| Li et al., 2008 | Gaussian dynamic BNs | Association | Bulb squeeze (healthy vs. Parkinsonian) | 
| Kim et al., 2008 | Discretized dynamic BNs | Association | Auditory task (schizophrenia vs. controls) | 
| Zhang et al., 2005 | Mixed dynamic BNs (HMMs) | Association | Monetary reward task (drug addicted vs. healthy) | 
| Rajapakse and Zhou, 2007 | Discretized dynamic BNs | Association | Silent reading and counting Stroop (normal subjects) | 
| Sun et al., 2012 | Gaussian BNs | Association | Watching videos (normal subjects) | 
| Neumann et al., 2010 | CPDAGs | Association | Meta-analysis | 
| Mitchell et al., 2004 | Gaussian naive Bayes | Sup. classification | Prediction of cognitive states | 
| Raizada and Lee, 2013 | Gaussian naive Bayes | Sup. classification | Distinction of phoneme sounds | 
| Ku et al., 2008 | Gaussian naive Bayes | Sup. classification | Prediction of which category a monkey is viewing | 
| Douglas et al., 2011 | Naive Bayes | Sup. classification | Belief vs. disbelief states | 
| Burge et al., 2009 | Discretized dynamic BNs | Association |  Healthy vs. demented elderly subjects | 
| Chen and Herskovits, 2007 | Inverse-tree classifier | Sup. classification | Young vs. non-demented vs. demented older|

<h4>BNs with MRI Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Joshi et al., 2010 | Gaussian BN | Association | Relationships between cortical surface areas | 
| Wang et al., 2013 | Gaussian BN | Association | Interaction graphs for AD patients and controls | 
| Chen et al., 2012a | Discretized dynamic BNs | Association | Temporal interactions in normal aging and MCI | 
| Duering et al., 2013 | Gaussian BN | Association | Processing speed deficits in VCI patients | 
| Morales et al., 2013 | Naive Bayes, selective naive Bayes|  Sup. classification | Early diagnosis of Parkinson’s disease | 
| Diciotti et al., 2012 | Naive Bayes | Sup. classification | Early diagnosis of AD | 
| Zhang et al., 2014 | Naive Bayes | Sup. classification | MCI vs. AD | 
| Chen et al., 2012b | Ensemble of BNs | Sup. classification | Conversion from MCI to Alzheimer | 

<h4>BNs with EEG Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Song et al., 2009 | Time-varying dynamic BNs | Association | Motor imagination task | 
| De la Fuente et al., 2011 | BN | Association | Borderline personality disorder | 
| Valenti et al., 2006 | Kernel naive Bayes | Sup. classification | Detection of interictal spikes (epilepsy)| 
| Acharya et al., 2011 | Naive Bayes | Sup. classification | Normal/interictal/ictal (epileptic) signals | 
| Rezaei et al., 2006 | HMM | Sup. classification|  Classification of mental states | 
| Speier et al., 2012|  Gaussian naive Bayes | Sup. classification | P300 Speller (virtual keyboard) | 
| Speier et al., 2014 | HMM | Sup. classification | P300 Speller (virtual keyboard) | 
| Zhang et al., 2006 | BN | Sup. classification | Hearing assessment and inference| 
| Hausfeld et al., 2012 |  Gaussian naive Bayes | Sup. classification | Speech sound identification (speakers and vowels) | 
| De Vico Fallani et al., 2011 | Gaussian naive Bayes | Sup. classification | Person identification (resting-state) | 

<h4>BNs with Other Data</h4>
| Researchers | BN model | Aim | Application |
| ----------- | -------- | --- | ----------- |
| Wang et al., 2011 | Gaussian naive Bayes | Sup. classification | Distinction of semantic categories (epilepsy) | 
| Goker et al., 2012 | Gaussian naive Bayes | Sup. classification | ME vs. healthy. | 
| Lu et al., 2014 | Gaussian selective naive Bayes | Sup. classification | Mental states (activation vs. rest) | 
| Dyrba et al., 2013 | Gaussian selective naive Bayes | Sup. classification | AD vs. controls | 
| Ayhan et al., 2013 | Gaussian selective naive Bayes | Sup. classification | Levels of dementia in AD | 
| Huang et al., 2011 | Sparse Gaussian BN | Association | Resting-state (AD vs. controls) | 

<h2>References</h2>
- [1] Bielza, C., Larranaga, P. "Bayesian networks in neuroscience: a survey"
- [2] Daly, R., Shen, Q., Aitken, S. "Learning Bayesian networks: approaches and issues"
- [3] Bielza, C., Li, G., Larranaga, P. "Multi-dimensional classification with Bayesian networks"
- [4] Pham, D., Ruz, G. "Unsupervised training of Bayesian networks for data clustering"








