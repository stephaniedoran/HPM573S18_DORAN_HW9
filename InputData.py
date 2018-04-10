# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

DELTA_T = 1/4       # years

PSA_ON = False      # if probabilistic sensitivity analysis is on

# transition matrix
TRANS_MATRIX = [
    [1500.0,  300.0,    0.0,    200.0],   # Well
    [0.0,     0.0,    2000.0,    0.0],   # STROKE
    [0.0,     500.0,    1100.0,   400.0],   # POST STROKE
    ]


# treatment relative risk
TREATMENT_RR = 0.65


