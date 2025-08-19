README

Disorder grouping:
Reports are organized per disorder / diagnosis.
Disorders were grouped together into a related categories. 
Note that this categorization is approximate (done heuristically) and does not reflect any strong claims about relationships between disorders. 


-- CLINICAL INFORMATION
Disease
	The clinical disorder which is the topic of study of the current report.
	Psychiatric and neurological disorders are all included, as well as brain injuries and/or other disorders that can affect brain function.
	Temporary state changes (e.g. intoxication or anesthesia) are not included.

-- BIBLIOGRAPHIC INFORMATION
Authors
	The authors, listed as APA style 'Last Name of First Author, et al'
	If there are multiple papers with the same first author, the second (or further) author(s) are also listed.
Year
	The year the report was published / released.
	The year listed here is the same as the year used to evaluate if the report is within the time range: the year the report was made available.
	This is typically the submission date for a preprint or the acceptance date / early-access data (for a journal article). 
	Note that dates used in the citation to a report may differ as these may refer to date of issue (inclusion in a volume) and so may be after the report was made available.
	Because of this, the listed dates do not necessarily correspond to order in which different reports were available and/or correspond to the citation for the report.
Month
	The month the report was published / released. Same notes as `year` for which date is listed.
DOI
	The digital object identifier (DOI) of the report.
Title
	The full title of the report.
Journal
	The journal the report appears in. 
	If a preprint, listed as 'preprint' (regardless of which preprint server). 

-- RECORDING INFORMATION
Data
	The electrophysiological data modality. 
	May list multiple modalities if multiple modalities included in the report. 
	Options: 
		EEG		- electroencephalography
		MEG		- magnetoencephalography
		DBS		- deep brain stimulation (recordings from the onboard electrodes)
		iEEG		- intracranial EEG (including grid, strip, and depth probes)
		RNS		- responsive neurostimulation (recordings from the onboard electrodes)
		multiple	- the report analyzes multiple different data modalities
Analyzed Data
	The 'state' / context of the data that is recorded / analyzed. 
	Options: 
		resting		- resting state, including both eyes open and eyes closed
		task		- data from during a task
		events		- events of interest e.g. seizure activity
		video		- participant is passively watching a video (no task)
		sleep		- recordings during sleep
		unconscious	- recordings made during an unconscious state
		intraoperative	- recordings made during during surgery, e.g. deep brain stimulation implantation
		baseline	- baseline segments extracted from a task context
		samples		- samples of recording extracted from ongoing recordings 
		movement	- recordings made while participant is moving
		meditation	- recordings made while participant is meditating
		unclear		- report does not clearly report information about data state

-- ANALYSIS INFORMATION
Amount of Data
	The amount of data included in the analysis. 
	If resting or similar state, this reflects the total reported amount of data included. 
	If task or similar, this reflects the length of each trial / event.
Design
	The design of the analysis.
	Options: 
		between 	- between subjects analysis
		within 		- within subjects analysis
		multiple	- includes both between and within subject analyses
Analysis
	The kind of analysis / comparison undertaken by the report. 
	May list multiple analyses if multiple relevant analyses are included in the report.
	Additional analyses may also be included in the paper that were not listed in the table.
	Options:
		diagnostic	- analysis comparing diagnostic categories, e.g. clinical group vs. control group 
		treatment	- analysis relates to the effect of treatment
		state		- analysis relates to comparing states e.g. seizure vs non-seizure
		symptoms	- analysis relates to symptom measures
		prognosis	- analysis relates to prognosis / progression / outcome of disease state
		region		- analysis compares activity across different regions
		at risk		- analysis of at-risk participants, comparing to future symptoms / diagnoses
		multiple	- analysis includes multiple different analyses


-- DATASET INFORMATION
# Patients
	The number of patients included in the clinical group.
Patient Ages
	The age information for the clinical group, in years.
	If original values not in years (e.g. months), values are converted.
	Possible formats for listing based on what is available:
		MEAN +/- STANDARD DEVIATION (if available, this format is preferred)
		MEAN [RANGE AS MIN_VALUE, MAX_VALUE]
		MEAN (MEASURE: VALUE)
			Measure explicitly stated in listed
				STE - standard error of the mean
				IQR - interquartile range
# Control
	The number of participants in the control group.
Control Ages
	The age information for the control group, if applicable. 
	Reporting conventions as in `Patient Ages`.

-- METHOD INFORMATION
Fit Method
	The analysis method used to estimate the aperiodic exponent.
	Options:
		specparam	- The 'spectral parameterization' (specparam; formerly fooof) method. Reference: Donoghue et al, 2020
		regression	- Regression model fit to the spectrum, typically linear fit to a log-log power spectrum.
				- Note that different studies listed as doing `regression` may employ different fitting approaches
		Colombo		- The fitting method as developed by the Colombo paper. Reference: Colombo et al, 2019
		irasa		- The 'irregular resampling & auto-spectral analysis' (IRASA) method. Reference: Wen & Liu, 2016
		eBOSC 		- The 'extended Better Oscillation Detector' method. Reference: Kosciessa et al, 2020
		Bódizs		- The fitting method as developed by the Bódizs paper.  Reference: Bódizs et al, 2021
		unclear		- The analysis method is not clearly reported.
Fit Range
	The frequency range, in Hz, that was analyzed for the aperiodic measure.
Report Settings
	Whether settings were reported for the fit method, if applicable.
	Reported as Yes / No. 
	Coded as Yes if some or all settings are reported - could be a partial report.
Report GOF
	Whether goodness-of-fit metrics (r-squared and/or fit error) were reported for the fit method, if applicable. 
	Reported as Yes / No.

-- RESULTS INFORMATION
Clinical EXP
	The reported exponent values for the clinical group (or clinical condition).
	These values are listed if report lists exact values for at least on comparison (reports may also include additional values). 
	Reports without this information listed may have approximate values displayed in figures. 
	Note that regardless of reported values in the paper (slope vs. exponent) - values are reported as exponent (positive values, larger magnitude is steeper spectrum).
Control EXP
	The reported exponent values for the control group (or control condition).
	Same conventions as in `Clinical EXP`.
Reported Finding
	The reported finding(s) of the paper - specifically any relating to the aperiodic exponent.
	If multiple relevant findings reported, then can include multiple findings, on separate lines.
	If different analyses use different subject groups / frequency ranges, etc, corresponding information can be in other cells on the same line.
	Shorthand notations:
		'w': with
		'vs.': versus, meaning compared to
	Symbols which are used:
		UP Arrow (⬆︎): increased exponent value (steepening)
		DOWN Arrow (⬇︎): decreased exponent value (flattening)
		Tilda (~): a relationship was found between (used to report continuous measures)
			Can be combined with an arrow - e.g. ⬆︎~X can be read as "an increased exponent is associated with a change in measure X"
		Triangle (Δ): indicates a change in measure, but without specifying the direction
			This can be used if the direction of the change is unclear and/or if there are multiple differences across the analysis
		No change symbol (∅): used to indicate no different between groups / no significant finding
	Results are described as succinctly as possible. In some cases, square brackets are used to add some detail, e.g. "⬇︎ w treatment [DRUG]" or "⬆︎ w stimulation [STIM-TYPE]"
		
Report Effects Size
	Whether the report includes any kind of effect size measure.
	Reported as Yes / No.
Effect Size Measure
	The measure used to report the effect size. 
	Options:
		cohen's-d			- Cohen's D standardized effect size measure
		eta-squared			- eta-squared effect size measure for ANOVAs
		z-score				- z-score measure of distribution / differences
		log(odds)			- logarithm of the odds ratio
		biserial rank correlation	- biserial rank correlation
		cohen's f^2			- cohen's effect size measure for F-test / ANOVA
		AUC				- area under the curve measure
Effects Size
	If reported, the actual value of the effect size measure. 
	Measure / units of this column defined in `Effect Size Measure`.
Biomarker
	Whether the paper discusses the aperiodic measures as a possible biomarker.
	Reported as Yes / No.
	Note that this reflects whether the feature is discussed as a biomarker, not the conclusion of the report on this point. 
Interpretation
	The main stated interpretation of the report of aperiodic activity, and the exponent specifically.
	By 'main' it means the primary interpretation that is reported - reports may discuss multiple interpretations.
	Having a listed interpretation does not necessarily mean the report explicitly endorses the stated interpretation. 
	Note that papers that do not list an interpretation may have motivated the aperiodic measure for methodological reasons.
	Options:
		E/I balance		- reflects the excitatory / inhibitory ratio
		slowing			- relative shift to 'slower' (lower frequency) activity
		neural noise		- relating to level of physiological 'noise' in the system / network / time series
		oscillations		- relating to the balance of different oscillatory frequencies / bands
		self-similarity		- relating to fractals / having an approximate similarity to oneself
		synchronicity		- degree of synchronicity of underlying activity
		complexity		- complexity of the time domain signal
		criticality		- relating to the criticality hypothesis (dynamical systems)
		timescale		- relating to the autocorrelation / characteristic timescale of the time series
		integration		- relating to the integration vs segregation of the neural circuit
		neurotransmission	- relating to the neurotransmission in the underlying circuit
		unstated		- no specific interpretation of aperiodic activity is stated
Notes
	Miscellaneous additional notes about the report.
	Adds information about the design / approach, subject groups, measures, analyses, and/or results. 
	This field may provide extra details if there are elements of the report that are hard to describe within the table
		e.g. multiple datasets, subgroup analyses, nuances to the findings, etc.
	If a piece of information is unclear (and marked as such in the table), this section may provide some more information
		e.g. a fit range may be unclear / not explicitly stated, but the notes may note an possible / approximate range based on visualizations or other information
	May also add some notes that are considered related but go beyond the details of the table (for example, other aperiodic features are also analyzed).
	There may also be notes on key themes / ideas / topics discussion points that are discussed in the paper.
