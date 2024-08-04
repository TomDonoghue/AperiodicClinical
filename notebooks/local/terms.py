""""Term definitions."""

####################################################################################################
####################################################################################################

TERMS = {

    # Set the aperiodic measure terms
    'AP' : [
        ['aperiodic exponent', 'spectral slope', '1/f slope', '1/f exponent'],
    ],

    # Set general clinical terms
    'CLINICAL' : [
        ['clinical'],
        ['disorder', 'disease'],
        ['biomarker'], 
        ['diagnosis', 'diagnostic'],
        ['treatment'],
    ],
    
    # Set disorder terms
    'DISORDERS' : [
        ["parkinson's"],
        ['epilepsy', 'seizure'],
        ['adhd', 'attention deficit hyperactivity disorder'],
        ['autism'],
        ['alzheimers', 'dementia'],
        ['disorders of consciousness', 'coma'],
        ['depression', 'MDD', 'major depressive disorder'],
        ['schizophrenia'],
        ['stroke'],
        ['tbi', 'traumatic brain injury'],
        ['dyslexia'],
        ['dystonia'],
        ['glioma'],
        ["huntington's"],
        ['multiple sclerosis'],
        ['ptsd', 'post traumatic stress disorder'],
        ['REM sleep behavior disorder'],
        ['rett syndrome'],
        ['ALS', 'amyotrophic lateral sclerosis', "Lou Gehrig's disease"],
        ['CDKL5 deficiency disorder'],
        ['chronic pain'],
        ['concussion'],
        ['down syndrome'],
        ['fibromyalgia'],
        ['fragile X'],
        ['insomnia'],
        ['nf1'],
        ['NREM parasomina'],
        ['OCD', 'obsessive compulsive disorder'],
        ['STXBP1'],
        ['tinnitus'],
        ['tourette syndrome'],
        ['tuberous sclerosis complex'],
    ],
}
    
# Define exclusion terms
EXCLUSIONS = ['acid', 'protein', 'ion', 'enzyme', 'ultrasound',
              'cancer', 'halide', 'spectroscopy', 'iodide', 'tissue']
