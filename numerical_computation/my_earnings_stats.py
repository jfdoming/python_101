import numpy
from numpy import genfromtxt

BASE_IDX = 2
LAST_IDX = 4
WAGE_IDX = 2 - BASE_IDX
HOURS_IDX = 3 - BASE_IDX
OT_IDX = 4 - BASE_IDX

data = genfromtxt(
    "earnings.csv",
    delimiter=",",
    skip_header=True,
    usecols=range(BASE_IDX, LAST_IDX + 1),
)


# Data processing.
earned = (
    data[:,WAGE_IDX] * data[:,HOURS_IDX]
    + 1.5 * data[:,WAGE_IDX] * data[:,OT_IDX]
)

# Statistics.
minimum = earned.min()
maximum = earned.max()
avg = earned.mean()
std = earned.std()

# Percentile.
pct_75_cutoff = numpy.percentile(earned, 75)
pct_75 = earned[earned > pct_75_cutoff]

# Output.
print("Minimum earned:", minimum)
print("Maximum earned:", maximum)
print("Average earned:", avg)
print("Standard deviation of earnings:", std)
print("Cutoff for 75th percentile:", pct_75_cutoff)
print("Earnings above 75th percentile:", pct_75)
