def countFunc(x):
    """Checks count to see if it is a multiple of 3, 5, or both

    Parameters
    ----------
    x : INT
        Values 0-100

    Returns
    -------
    name : STRING or INT
        Returns a string if the count is a multiple of 3, 5, or both
        and returns an int (the count) otherwise
    """
    
    if x % 3 == 0 and x % 5 == 0:
        return "Fizz" +  " Buzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

if __name__ == '__main__':
    y = [countFunc(x) for x in xrange(101)]
    print (y)
