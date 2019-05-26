import numpy as np
from scipy.stats import rv_discrete


# Source https://github.com/scipy/scipy/issues/6000#issuecomment-359051189
class pbinom(rv_discrete):
    """A  Poisson binomial discrete random variable.

    %(before_notes)s

    Notes
    -----
    Probability distribution of a series of independent Bernoulli
    random variables that are not necessarily identically distributed.

    For details see: http://en.wikipedia.org/wiki/Poisson_binomial_distribution

    `pbinom` takes ``probabilities``, an array of probabilities for the Bernoulli
    variables as parameters.

    %(after_notes)s

    %(example)s

    """
    def __init__(self, probabilities, seed=None):
        self.probabilities = np.asarray(probabilities)
        if not ((self.probabilities <= 1).all() and (self.probabilities >= 0).all()):
            raise ValueError("All probabilities must be between 0 and 1")
        super(pbinom, self).__init__(seed=seed, a=0, b=len(probabilities))

    def _rvs(self):
        n = self._size
        return sum((self._random_state.binomial(1, p) for p in self.probabilities))

    def _pmf(self, x):
        n = len(self.probabilities)
        C = np.exp(2j*np.pi/(n+1))
        s = 0
        for l in range(0, n+1):
            product = 1
            for p in self.probabilities:
                product *= 1 + (C**l - 1) * p
            s += C**(-l*x) * product
        return 1/(n+1) * s.real
