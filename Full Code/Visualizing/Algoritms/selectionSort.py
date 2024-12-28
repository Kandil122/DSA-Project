
import time
from colors import *

def selection_sort(data, start, end, drawData, timeTick):
    size=len(data)
    for i in range(size):
        minIndex=i
        for j in range(i+1, size):
            if data[j]<data[minIndex]:
                minIndex=j
        temp=data[i]
        data[i]=data[minIndex]
        data[minIndex]=temp

        drawData(data, [RED if x == j or x == j+1 else BLUE for x in range(len(data))] )
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
