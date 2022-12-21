import numpy as np
import scipy.stats as stats

# criar arrays a partir de lista de valores
x=np.array([0.880, 1.054, 0.866, 0.883, 0.913, 0.893, 0.872, 0.949, 0.848, 0.907, 0.852, 0.901, 0.935, 0.945, 0.999, 0.995])
y=np.array([0.894, 1.113, 0.908, 0.946, 0.976, 0.929, 0.870, 0.941, 0.864, 0.990, 0.845, 0.930, 1.010, 0.871, 0.974, 0.917])

# teste shapiro
print(stats.shapiro(x-y))

# t.test
stats.ttest_rel(x,y,alternative="less")
