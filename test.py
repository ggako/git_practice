

def median(x, y, z):
    """
    Returns the median of 3 provided integers
    Parameters:
        x, y, z (int): data values
    Returns:
        array[1] (int): median of data values
    NOTE: Median is the middle number after ordering        
    """
    array = [x, y, z]
    array.sort()

    return array[1]

x = 2
y = 3
w = 3
print(f"he medan of {x}, {y} and {w} is {median(x, y, w)}")