def myaverage(l:list)->float:
    """
    Calculate the average of list l
    
    Examples:
    
    >>> myaverage([1,2])
    1.5
    
    """
    n = len(l)
    if n==0:
        raise ValueError("cant calculate mean of length 0 list")
    try:
        thesum = sum(l)
    except:
        raise TypeError("Cannot sum things of different types")
    average = thesum/n
    return average