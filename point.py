def getPoints(n):
    n = (n-1) % 13 + 1
    #the ace values
    if n == 1:
        return [1,11]
    #the regular card values
    if 2<=n<=10:
        return [n]
    if 11<=n<=13:
        return [10]