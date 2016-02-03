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

</|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> DeFelipe et al., 2013 </sub>|<sub> BN and naive Bayes </sub>|<sub> Assoc. and supervised class </sub>|<sub> Classification and naming of GABAergic interneurons </sub>|<sub>
</sub>|<sub> Lopez-Cruz et al., 2014 </sub>|<sub> BN and BN multinet </sub>|<sub> Assoc. and inference and cluster </sub>|<sub> Consensus model for interneuron classification </sub>|<sub>
</sub>|<sub>Mihaljevic et al., in press </sub>|<sub> Naive Bayes and TAN </sub>|<sub> Supervised class </sub>|<sub> Classification of cortical GABAergic interneurons </sub>|<sub>
</sub>|<sub>Mihaljevic et al., Under review </sub>|<sub> MBC </sub>|<sub> Multi-dimensional class </sub>|<sub> Simultaneous classification of six axonal class variables </sub>|<sub>
</sub>|<sub>Guerra et al., 2011 </sub>|<sub> Naive Bayes </sub>|<sub> Supervised class </sub>|<sub> Pyramidal neuron vs. interneuron </sub>|<sub>
</sub>|<sub>Lopez-Cruz et al., 2011 </sub>|<sub> BN </sub>|<sub> Inference, associations </sub>|<sub> Model and simulation of dendritic trees </sub>|<sub>

<h4>BNs with Electrophysical Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Smith et al., 2006 </sub>|<sub> Dynamic BN </sub>|<sub> Association </sub>|<sub> Infer non-linear neural information flow networks </sub>|<sub>
</sub>|<sub> Eldawlatly et al., 2010 </sub>|<sub> Dynamic BN </sub>|<sub> Association </sub>|<sub> Infer effective and time-varying connectivity between spiking cortical neurons </sub>|<sub>
</sub>|<sub> Jung et al., 2010 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> Neuronal synchrony from electrode signal recordings </sub>|<sub>
</sub>|<sub> Pecevski et al., 2011 </sub>|<sub> BN </sub>|<sub> Inference </sub>|<sub> Emulate probabilistic inference through networks of spiking neurons </sub>|<sub>

<h4>BNs with 'Omics Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Armañanzas et al., 2012 </sub>|<sub> Ensemble of BN classifiers </sub>|<sub> Association </sub>|<sub> Transcripts in AD </sub>|<sub>
</sub>|<sub> Hullam et al., 2012 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> SNPs in depression </sub>|<sub>
</sub>|<sub> Zeng et al., 2013 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> Cytokines and mRNA in cerebral ischemia </sub>|<sub>
</sub>|<sub> Liang et al., 2007 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> SNPs in childhood absence epilepsy </sub>|<sub>
</sub>|<sub> Zhang et al., 2010 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> Regulation network of the neuron-specific factor Nova (mice) </sub>|<sub>
</sub>|<sub> Jiang et al., 2011 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> SNPs in late onset AD </sub>|<sub>
</sub>|<sub> Han et al., 2012 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> SNPs in early onset autism </sub>|<sub>
</sub>|<sub> Wei et al., 2011 </sub>|<sub> Model-averaged NB, selective NB </sub>|<sub>Sup. classification </sub>|<sub> Prediction of AD from SNPs </sub>|<sub>
</sub>|<sub> Gollapalli et al., 2012 </sub>|<sub> Selective NB </sub>|<sub> Sup. classification </sub>|<sub> Mass spectrometry for predicting glioblastoma </sub>|<sub>
</sub>|<sub> Belgard et al., 2011 </sub>|<sub> Naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Distinguish sequenced transcriptomes among layers I-VIb </sub>|<sub>

<h4>BNs with fMRI Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Iyer et al., 2013 </sub>|<sub> Gaussian BNs </sub>|<sub> Association </sub>|<sub> Resting-state (normal subjects)</sub>|<sub> 
</sub>|<sub> Dawson et al., 2013 </sub>|<sub> Gaussian BNs </sub>|<sub> Association </sub>|<sub> Resting-state (normal subjects)</sub>|<sub> 
</sub>|<sub> Li et al., 2011 </sub>|<sub> Gaussian BNs </sub>|<sub> Association </sub>|<sub> Resting-state (normal subjects)</sub>|<sub> 
</sub>|<sub> Li et al., 2013 </sub>|<sub> Gaussian BNs </sub>|<sub> Association </sub>|<sub> Resting-state (aMCI vs. controls)</sub>|<sub> 
Labatut et al., 2004 </sub>|<sub> Gaussian dynamic BNs </sub>|<sub> Association </sub>|<sub> Phoneme task (normal vs. dyslexic) </sub>|<sub> 
</sub>|<sub> Li et al., 2008 </sub>|<sub> Gaussian dynamic BNs </sub>|<sub> Association </sub>|<sub> Bulb squeeze (healthy vs. Parkinsonian) </sub>|<sub> 
</sub>|<sub> Kim et al., 2008 </sub>|<sub> Discretized dynamic BNs </sub>|<sub> Association </sub>|<sub> Auditory task (schizophrenia vs. controls) </sub>|<sub> 
</sub>|<sub> Zhang et al., 2005 </sub>|<sub> Mixed dynamic BNs (HMMs) </sub>|<sub> Association </sub>|<sub> Monetary reward task (drug addicted vs. healthy) </sub>|<sub> 
</sub>|<sub> Rajapakse and Zhou, 2007 </sub>|<sub> Discretized dynamic BNs </sub>|<sub> Association </sub>|<sub> Silent reading and counting Stroop (normal subjects) </sub>|<sub> 
</sub>|<sub> Sun et al., 2012 </sub>|<sub> Gaussian BNs </sub>|<sub> Association </sub>|<sub> Watching videos (normal subjects) </sub>|<sub> 
</sub>|<sub> Neumann et al., 2010 </sub>|<sub> CPDAGs </sub>|<sub> Association </sub>|<sub> Meta-analysis </sub>|<sub> 
</sub>|<sub> Mitchell et al., 2004 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Prediction of cognitive states </sub>|<sub> 
</sub>|<sub> Raizada and Lee, 2013 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Distinction of phoneme sounds </sub>|<sub> 
</sub>|<sub> Ku et al., 2008 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Prediction of which category a monkey is viewing </sub>|<sub> 
</sub>|<sub> Douglas et al., 2011 </sub>|<sub> Naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Belief vs. disbelief states </sub>|<sub> 
</sub>|<sub> Burge et al., 2009 </sub>|<sub> Discretized dynamic BNs </sub>|<sub> Association </sub>|<sub>  Healthy vs. demented elderly subjects </sub>|<sub> 
</sub>|<sub> Chen and Herskovits, 2007 </sub>|<sub> Inverse-tree classifier </sub>|<sub> Sup. classification </sub>|<sub> Young vs. non-demented vs. demented older</sub>|<sub>

<h4>BNs with MRI Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Joshi et al., 2010 </sub>|<sub> Gaussian BN </sub>|<sub> Association </sub>|<sub> Relationships between cortical surface areas </sub>|<sub> 
</sub>|<sub> Wang et al., 2013 </sub>|<sub> Gaussian BN </sub>|<sub> Association </sub>|<sub> Interaction graphs for AD patients and controls </sub>|<sub> 
</sub>|<sub> Chen et al., 2012a </sub>|<sub> Discretized dynamic BNs </sub>|<sub> Association </sub>|<sub> Temporal interactions in normal aging and MCI </sub>|<sub> 
</sub>|<sub> Duering et al., 2013 </sub>|<sub> Gaussian BN </sub>|<sub> Association </sub>|<sub> Processing speed deficits in VCI patients </sub>|<sub> 
</sub>|<sub> Morales et al., 2013 </sub>|<sub> Naive Bayes, selective naive Bayes</sub>|<sub>  Sup. classification </sub>|<sub> Early diagnosis of Parkinson’s disease </sub>|<sub> 
</sub>|<sub> Diciotti et al., 2012 </sub>|<sub> Naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Early diagnosis of AD </sub>|<sub> 
</sub>|<sub> Zhang et al., 2014 </sub>|<sub> Naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> MCI vs. AD </sub>|<sub> 
</sub>|<sub> Chen et al., 2012b </sub>|<sub> Ensemble of BNs </sub>|<sub> Sup. classification </sub>|<sub> Conversion from MCI to Alzheimer </sub>|<sub> 

<h4>BNs with EEG Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Song et al., 2009 </sub>|<sub> Time-varying dynamic BNs </sub>|<sub> Association </sub>|<sub> Motor imagination task </sub>|<sub> 
</sub>|<sub> De la Fuente et al., 2011 </sub>|<sub> BN </sub>|<sub> Association </sub>|<sub> Borderline personality disorder </sub>|<sub> 
</sub>|<sub> Valenti et al., 2006 </sub>|<sub> Kernel naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Detection of interictal spikes (epilepsy)</sub>|<sub> 
</sub>|<sub> Acharya et al., 2011 </sub>|<sub> Naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Normal/interictal/ictal (epileptic) signals </sub>|<sub> 
</sub>|<sub> Rezaei et al., 2006 </sub>|<sub> HMM </sub>|<sub> Sup. classification</sub>|<sub>  Classification of mental states </sub>|<sub> 
</sub>|<sub> Speier et al., 2012</sub>|<sub>  Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> P300 Speller (virtual keyboard) </sub>|<sub> 
</sub>|<sub> Speier et al., 2014 </sub>|<sub> HMM </sub>|<sub> Sup. classification </sub>|<sub> P300 Speller (virtual keyboard) </sub>|<sub> 
</sub>|<sub> Zhang et al., 2006 </sub>|<sub> BN </sub>|<sub> Sup. classification </sub>|<sub> Hearing assessment and inference</sub>|<sub> 
</sub>|<sub> Hausfeld et al., 2012 </sub>|<sub>  Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Speech sound identification (speakers and vowels) </sub>|<sub> 
</sub>|<sub> De Vico Fallani et al., 2011 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Person identification (resting-state) </sub>|<sub> 

<h4>BNs with Other Data</h4>
</sub>|<sub> Researchers </sub>|<sub> BN model </sub>|<sub> Aim </sub>|<sub> Application </sub>|<sub>
</sub>|<sub> ----------- </sub>|<sub> -------- </sub>|<sub> --- </sub>|<sub> ----------- </sub>|<sub>
</sub>|<sub> Wang et al., 2011 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Distinction of semantic categories (epilepsy) </sub>|<sub> 
</sub>|<sub> Goker et al., 2012 </sub>|<sub> Gaussian naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> ME vs. healthy. </sub>|<sub> 
</sub>|<sub> Lu et al., 2014 </sub>|<sub> Gaussian selective naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Mental states (activation vs. rest) </sub>|<sub> 
</sub>|<sub> Dyrba et al., 2013 </sub>|<sub> Gaussian selective naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> AD vs. controls </sub>|<sub> 
</sub>|<sub> Ayhan et al., 2013 </sub>|<sub> Gaussian selective naive Bayes </sub>|<sub> Sup. classification </sub>|<sub> Levels of dementia in AD </sub>|<sub> 
</sub>|<sub> Huang et al., 2011 </sub>|<sub> Sparse Gaussian BN </sub>|<sub> Association </sub>|<sub> Resting-state (AD vs. controls) </sub>|<sub> 

<h2>References</h2>
- [1] Bielza, C., Larranaga, P. "Bayesian networks in neuroscience: a survey"
- [2] Daly, R., Shen, Q., Aitken, S. "Learning Bayesian networks: approaches and issues"
- [3] Bielza, C., Li, G., Larranaga, P. "Multi-dimensional classification with Bayesian networks"
- [4] Pham, D., Ruz, G. "Unsupervised training of Bayesian networks for data clustering"








