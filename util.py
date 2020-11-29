"""Common Data Definitions"""


class Node(object):
    def __init__(self):
        self.dict = {'N': None, 'E': None, 'S': None, 'W': None}

    def __iter__(self):
        return iter(self.dict)


class Directions(object):
    """Iterable where each element is in {'N', 'E', 'S', 'W'}."""
    def __init__(self, *args):
        for arg in args:
            assert arg in 'NESW'
        self.list = args

    def __iter__(self):
        return iter(self.list)
