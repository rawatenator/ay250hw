import numpy.linalg as lin
import numpy as np


def matrixinv(array):
    '''supply array, will return inverse if it is square and det !=0'''
    r,c = np.shape(array)
    
    if (lin.det(array) != 0) and (r == c) : #check if the input array has non0 det
                                            #check if the input is square
        
        Identity = np.eye(r)                #np.eye(x) produces the identity matrix, w/x rows
        return lin.solve(a,Identity)           #solve function computes the inverse
        
    else:
        print "not sq and/OR det doesn't = 0"




# Array, "a," is what we want to invert

a = np.array([[1,2,3,4],[1,2,4,4],[4,4,2,4],[1,2,3,7]]) 
print matrixinv(a)



### TO CHECK OUTPUT, COMPARE VALUES TO THE INV FUNCTION IN NUMPY:
print lin.inv(a)
