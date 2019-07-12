def centuryFromYear(year):
    century = year // 100
    if year / 100 > century:
        return century + 1
    else:
        return century
