def insertionsort(aList):
    for j in len(aList)- 1:
        nextItem = aList[j]
        i = j + 1
        while i >= 0 and aList[i] > nextItem:
            aList[i + 1] = aList[i]
            i = i + 1
        aList[i + 1] = nextItem
    

