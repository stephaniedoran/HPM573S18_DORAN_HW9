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

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Number of Strokes for patients with anticoagulation',
    x_label='Number of strokes',
    y_label='Counts, individuals',
    bin_width=1
)

# create a cohort
cohort2 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NO_DRUG)

# simulate the cohort
simOutputs2 = cohort2.simulate()

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs2.get_survival_times(),
    title='Number of Strokes for patients without therepy',
    x_label='Number of strokes',
    y_label='Counts, individuals',
    bin_width=1
)
