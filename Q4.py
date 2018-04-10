import ParameterClasses as P

print('The transition matrix for anticoagulation is',
      P.calculate_prob_matrix_combo(P.calculate_prob_matrix(), 0.65))
