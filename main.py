# GRADED FUNCTION: T_stretch
import numpy as np


# GRADED FUNCTION: T_hshear

def T_hshear(m, v):
    """
    Performs a 2D horizontal shearing transformation on an array v using a shearing factor m.

    Args:
        m (float): The shearing factor.
        v (np.array): The array to be sheared.

    Returns:
        np.array: The sheared array.
    """

    ### START CODE HERE ###
    # Define the transformation matrix
    T = np.array([[1, m],
                  [0, 1]])

    w = T @ v

    ### END CODE HERE ###

    return w


arr=np.array([[1,2],[9,1],[0,2]])
print(T_hshear(3,arr))
#We will now be working the a nural newtowk of a single newuron suppose we have a z=Wx+b 
#wheer wx is the dot product of weights and independent variable 
#[w1 w2].[[x11...x1n],[x21...x2n]] we also have bias b as scalar
"""
cost cuntion"""