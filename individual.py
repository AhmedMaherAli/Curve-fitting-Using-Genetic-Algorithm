import numpy.random as rand
class Individual(object):   

    def __init__(self, coefficients):
        # Generate normal distributed coefficients for each variable plus the intercept
        self.values = [rand.uniform(-2,2) for _ in range(coefficients + 1)] 
        self.fit = None


