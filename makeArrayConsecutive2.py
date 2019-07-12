def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    for i in range(len(statues) - 1):
        if statues[i]+1 != statues[i+1]:
            count += (statues[i+1] - statues[i]) - 1
        else:
            continue
    return count
