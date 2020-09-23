def index(array, n):
    length = len(array)
    if(n > length - 1):
        return -1
    item = array[n]
    return item ** n;