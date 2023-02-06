import numpy as np

def missing(array):
    arr = np.isnan(array)
    return array[np.logical_not(arr)]



arr =np.array([1,2,3,np.nan,5,6,7,np.nan])
print(missing(arr))
