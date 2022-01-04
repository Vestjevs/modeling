from scipy import integrate

import numpy as np

# phi - пористость
# mu - вязкость
# c - общая сжимаемость системы
# k - проницаемость

phi, mu, c, k, h = 0.0, 0.1, 0.1, 0.1, 0.1
p_0 = 1.3
Q_0 = 0.4

XI = phi * mu * c / k

f = lambda t: np.exp(-t) / t

expint = lambda x: integrate.quad(f, x / (4 * 1), np.inf)[0]

p = lambda x: p_0 + (mu * Q_0) / (4 * np.pi * k) * expint(x)
