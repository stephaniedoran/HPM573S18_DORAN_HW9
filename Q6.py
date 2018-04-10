import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAGULATION)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve, Anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# create a cohort
cohort2 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NO_DRUG)

# simulate the cohort
simOutputs2 = cohort2.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve, no drug',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )
