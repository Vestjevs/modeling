from scipy import integrate

import numpy as np


# mu - вязкость
# c - общая сжимаемость системы
# k - проницаемость

class Element:
    def __init__(self, r, k, c, mu):
        self.q = []
        self.r = r
        self.k = k
        self.c = c
        self.mu = mu

    def coef1(self):
        return 4 * self.k / (self.c * self.mu)

    def coef2(self):
        return self.mu / (4 * np.pi * self.k)

    def generate_q(self):
        self.q.append(np.random.randint(1, 25))
        self.q.sort()


f = lambda t: np.exp(-t) / t
expint = lambda x: integrate.quad(f, x, np.inf)[0]


def find_summand(element, r, t, t_i):
    res = 0
    q = element.q
    for i in range(1, len(q)):
        arg = (r - element.r) / (element.coef1() * (t - t_i[i - 1]))
        res += (q[i] - q[i - 1]) * expint(arg)

    return -res


def P(r, T, p_0, elements, t_i):
    res = p_0

    for elem in elements:
        res += elem.coef2() * find_summand(elem, r, T, t_i)

    return res
