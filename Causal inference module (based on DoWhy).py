from dowhy import CausalModel
import pandas as pd

def build_causal_model(data, treatment, outcome):

    model = CausalModel(
        data=data,
        treatment=treatment,
        outcome=outcome,
        graph="digraph { treatment -> outcome; confounder -> treatment; confounder -> outcome; }"
    )
    identified_estimand = model.identify_effect()
    estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")
    return estimate.value


local_data = pd.DataFrame(X_train, columns=data.feature_names)
local_data['outcome'] = y_train
treatment_var = 'mean radius'  
causal_effect = build_causal_model(local_data, [treatment_var], 'outcome')
print(f"Causal Effect of {treatment_var}: {causal_effect}")