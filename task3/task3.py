import sys
import pandas as pd
import argparse as argp

#https://ergoz.ru/razbor-parametrov-komandnoy-stroki-v-python/
def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-d', '--dir', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

Queue1 = [float(x.rstrip()) for x in open(namespace.dir + "/Cash1.txt")]
Queue2 = [float(x.rstrip()) for x in open(namespace.dir + "/Cash2.txt")]
Queue3 = [float(x.rstrip()) for x in open(namespace.dir + "/Cash3.txt")]
Queue4 = [float(x.rstrip()) for x in open(namespace.dir + "/Cash4.txt")]
Queue5 = [float(x.rstrip()) for x in open(namespace.dir + "/Cash5.txt")]

QueueAll = []
counter = 0
while counter < 16:
    C = Queue1[counter] + Queue2[counter] + Queue3[counter] + Queue4[counter] + Queue5[counter]
    QueueAll.append(C)
    counter += 1
print(pd.Series(QueueAll).idxmax()+1)
