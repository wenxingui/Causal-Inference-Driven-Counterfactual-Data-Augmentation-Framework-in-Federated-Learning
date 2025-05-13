from sdv.tabular import GaussianCopula

class CounterfactualGenerator:
    def __init__(self, data, treatment_var):
        self.model = GaussianCopula()
        self.model.fit(data)
        self.treatment_var = treatment_var
        
    def generate_counterfactuals(self, intervention_value, num_samples=100):
        synthetic_data = self.model.sample(num_samples)
        synthetic_data[self.treatment_var] = intervention_value 
        return synthetic_data


generator = CounterfactualGenerator(local_data, treatment_var)
cf_data = generator.generate_counterfactuals(intervention_value=10.0)