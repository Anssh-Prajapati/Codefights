def arrayMaximalAdjacentDifference(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)