from __future__ import annotations

from typing import AbstractSet
from typing import List
from typing import Tuple
from typing import Union
from typing import TypeVar
from typing import Iterable

AllowedContainers = Union[List, Tuple, AbstractSet]

T = TypeVar('T', int, float, complex)
Vec = Iterable[Tuple[T,T]]

def print_container_values(container: AllowedContainers):
    '''print container values

    Args:
        container (AllowedContainers): a value that can be a list, tuple or set

    '''
    for val in container:
        print(val)

def inner_product(v: Vec[T]) -> T:
    return sum(x*y for x,y in v)


def main():
    l1 = [1,2,3]
    print_container_values(l1)
    d1 = {'a':1,'b':2}
    print_container_values(d1)
    t1 = (1,2,3)
    print_container_values(t1)


    v1 = [(1.0,1), (2,2)]
    print(inner_product(v1))



if __name__ == "__main__":
    main()