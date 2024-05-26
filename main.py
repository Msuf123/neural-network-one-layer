# GRADED FUNCTION: T_stretch
import numpy as np


def T_stretch(a, v):
    """
    Performs a 2D stretching transformation on a vector v using a stretching factor a.

    Args:
        a (float): The stretching factor.
        v (numpy.array): The vector (or vectors) to be stretched.

    Returns:
        numpy.array: The stretched vector.
    """

    ### START CODE HERE ###
    # Define the transformation matrix
    T = np.array([[1*a,0],[0,1*a]])

    # Compute the transformation
    w = v @ T
    ### END CODE HERE ###

    return w
arr=np.array([[1,2],[3,4]])
print(T_stretch(3,arr))