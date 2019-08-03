import sys
import math
import numpy as np
import argparse as argp

#https://ergoz.ru/razbor-parametrov-komandnoy-stroki-v-python/
def createParser():
    parser = argp.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

#http://qaru.site/questions/952/how-do-i-read-a-file-line-by-line-into-a-list
skorr = [float(x.rstrip()) for x in open(namespace.name)]
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
