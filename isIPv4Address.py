def isIPv4Address(inputString):
    p = inputString.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
            