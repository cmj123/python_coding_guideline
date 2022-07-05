'''Own implementation of a 2D vector class
'''

from __future__ import annotations
import numpy as np

import numbers
from functools import total_ordering
from math import sqrt 
from typing import SupportsFloat
from typing import Union

# @total_ordering
class Vector2D:
    '''Vector2D class to perform simple vector operations
    '''

    def __init__(self, x: SupportsFloat =0, y: SupportsFloat = 0) -> None:
        '''Create a vector instance with the given x and y values

        Args:
            x (SupportsFloat, optional): x-Value. Defaults to 0.
            y (SupportsFloat, optional): y-Value. Defaults to 0.

        Raises:
            TypeError: If x or y are not a number
        '''
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')

    
    def __call__(self) -> str:
        '''Callable for the vector instance representation.

        Returns:
            str: The representation of the vector instance.
        '''
        print('Calling the __call__ function!')
        return self.__repr__()

    
    def __repr__(self) -> str:
        '''The vector instance as a string

        Returns:
            str: The representation of the vector instance 
        '''

        return f'vector.Vector2D({self.x}, {self.y})'

    def __str__(self) -> str:
        '''The vector instance as a string

        Returns:
            str: The vector instance as a string
        '''
        return f'({self.x}, {self.y})'

    def __bool__(self) -> bool:
        '''Return the truth value of the vector instance

        Returns:
            bool: True, if the vector is not a null-vector. False, else
        '''
        if np.isnan(self.x) and np.isnan(self.y):
            return False
        return True
    


if __name__ == "__main__":
    my_vector = Vector2D(1,np.nan)
    # print(my_vector())
    # print(str(my_vector))
    # print(repr(my_vector))
    print(bool(my_vector))
