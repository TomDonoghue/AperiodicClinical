""""Term definitions."""

####################################################################################################
####################################################################################################

TERMS = {

    # Set the aperiodic measure terms
    'AP' : [
        [
            'aperiodic exponent',
            'aperiodic slope',
            'spectral exponent',
            'spectral slope',
            '1/f slope',
            '1/f exponent',
        ],
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
        ['ADHD', 'attention deficit hyperactivity disorder'],
        ['autism', 'ASD'],
        ['alzheimers', 'dementia'],
        ['disorders of consciousness', 'coma', 'locked-in'],
        ['depression', 'MDD', 'major depressive disorder'],
        ['schizophrenia'],
        ['stroke'],
        ['dystonia'],
        ['TBI', 'traumatic brain injury'],
        ['dyslexia'],
        ['glioma'],
        ["huntington's"],
        ['multiple sclerosis'],
        ['PTSD', 'post traumatic stress disorder'],
        ['REM sleep behavior disorder'],
        ['rett syndrome'],
        ['22q.11.2'],
        ['ALS', 'amyotrophic lateral sclerosis', "Lou Gehrig's disease"],
        ['anxiety'],
        ['CDKL5 deficiency disorder'],
        ['chronic pain'],
        ['concussion'],
        ['down syndrome'],
        ['fibromyalgia'],
        ['fragile X'],
        ['insomnia'],
        ['NF1'],
        ['NREM parasomina'],
        ['OCD', 'obsessive compulsive disorder'],
        ['STXBP1'],
        ['tinnitus'],
        ['tourette'],
        ['tuberous sclerosis complex'],
        ['delirium'],
        ['stutter'],
        ['cancer'],
    ],
}

# Define exclusion terms
EXCLUSIONS = ['acid', 'protein', 'ion', 'enzyme', 'ultrasound',
              'cancer', 'halide', 'spectroscopy', 'iodide', 'tissue']
