# https://gist.github.com/f00-/a835909ffd15b9927820d175a48dee41

import numpy as np
import matplotlib.pyplot as plt

def ApEn(U, m, r):
    """Calculates the approximate entropy of U.
    
        Args:
            U: time-series signal
            m: length of comparison data
            r: filtering level
        Returns:
            the apen-value.
    """

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / 
             (N - m + 1.0) for x_i in x]
        return (N - m + 1.0)**(-1) * sum(np.log(C))

    N = len(U)

    return abs(_phi(m + 1) - _phi(m))

def debug_ApEn(ts, m = 2, r = 3):
    plt.plot(ts)
    plt.title('ApEn = {0}'.format(ApEn(ts, 2, 3)))
    plt.show()

# Usage example
U = np.array([85, 80, 89] * 17)
debug_ApEn(U)

# 1.0996541105257052e-05