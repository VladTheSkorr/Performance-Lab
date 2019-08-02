import math
import numpy as np

skorr = [float(i) for i in input().split()]
new = sorted(skorr)

def mediana(skorr):
    l = int(len(new) / 2)
    if len(new) % 2 != 0:
        return new[l]
    else:
        return (new[l] + new[l - 1]) / 2.0
print(np.percentile(new, 90))
print(mediana(skorr))
print(max(new))
print(min(new))
print(sum(new) / len(new))