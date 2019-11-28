"""
    Author: @elnaztaqizadeh
    License: BSD
    The result and figure of this code is published in the Critique of bourdieusian
    methodology based on a comparative study of Iran’s konkoor (National university
    entrance exam) (2019)
    For more information, see https://github.com/ElnazTaqizadeh/MachineLearning/ConcoursScoreDist.py
    To report a bug or issue, create an issue on https://github.com/ElnazTaqizadeh/MachineLearning/issues.
"""

# Matplotlib: Python 2D plotting library 
# NumPy: Fundamental package for scientific computing with Python.
#scipy.stats: Scipy module contains a large number of probability distributions
# as well as a growing library of statistical functions.
#scipy.stats.skewnorm: A skew-normal random variable.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm

# mean, variance, skewness, kurtosis, Maxwell constant
mean =  19.73
var = 7.9
skew = 5.109
kurt = 25.030
a = 5.109


# The loc parameter always shifts the x variable. 
# It generalizes the distribution to allow shifting x=0 to x=loc. 
# the scale corresponds to the parameter a in the equation
loc, scale = -1.0, 20.0

# Generate random numbers
data = skewnorm(a, loc, scale).rvs(100)

# Parameter estimates for generic data
ae, loce, scalee = skewnorm.fit(data)

# Begin plotting
plt.figure()

xmin, xmax  = -10, 100

# Display the probability density function (pdf)
x = np.linspace(xmin, xmax, 100)
p = skewnorm.pdf(x,ae, loce, scalee)
plt.plot(x, p, 'k', linewidth=2)

# Compare the histogram
plt.hist(data, bins=100, normed=True, alpha=0.6, color='g')