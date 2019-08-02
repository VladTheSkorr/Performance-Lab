import pandas as pd

Queue1 = [1, 1.2, 1.4, 1.7, 1.9, 2.7, 4.7, 4.4, 4.2, 3.4, 2.4, 1.1, 4.5, 1.3, 3.4, 1]
Queue2 = [1, 1.2, 1.4, 1.7, 1.9, 2.7, 4.7, 4.4, 4.2, 3.4, 2.4, 1.1, 4.5, 1.3, 3.4, 1]
Queue3 = [1, 1.2, 1.4, 1.7, 1.9, 2.7, 4.7, 4.4, 4.2, 3.4, 2.4, 1.1, 4.5, 1.3, 3.4, 1]
Queue4 = [1, 1.2, 1.4, 1.7, 1.9, 2.7, 4.7, 4.4, 4.2, 3.4, 2.4, 1.1, 4.5, 1.3, 3.4, 1]
Queue5 = [1, 1.2, 1.4, 1.7, 1.9, 2.7, 4.7, 4.4, 4.2, 3.4, 2.4, 1.1, 4.5, 1.3, 3.4, 1]

QueueAll = []

counter = 0
while counter < 16:
    C = Queue1[counter] + Queue2[counter] + Queue3[counter] + Queue4[counter] + Queue5[counter]
    QueueAll.append(C)
    counter += 1
print(pd.Series(QueueAll).idxmax()+1)