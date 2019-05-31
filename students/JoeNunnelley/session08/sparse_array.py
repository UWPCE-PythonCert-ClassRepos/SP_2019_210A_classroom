#! /usr/bin/env python3

"""
Impementation of a sparse array
Author : Joe Nunnelley
"""
class SparseArray:
    """
    A class to store an array more efficiently by only storing the initialized elements
    and inferring the uninitialized items.
    """
    def __init__(self, arr):
        """
        Initialize the array to a dict so we only have to store non-zero pairs
        """
        self.storage = dict()
        self.size = 0

        for index, item in enumerate(arr):
            self.size = len(arr)

            if item != 0:
                self.storage[index] = item


    def append(self, key, value):
        """
        Append a key value pair to the array
        """
        self.__setitem__(key, value)
        return self.storage


    def __len__(self):
        """
        Get the length of the reconstituted array
        """
        return self.size


    def __getitem__(self, key):
        """
        Get an item from the array when requested using the [] notation
        """
        if isinstance(key, slice):
            slicedkeys = list(self.storage.keys())[key]
            return {k: self.storage[k] for k in slicedkeys}
        elif isinstance(key, int):
            try:
                return self.storage[key]
            except KeyError:
                return 0
        else:
            return 0


    def __setitem__(self, key, value):
        """
        Set an item in the array using the [] notation.
        Only extend the array size if the value is 0
        """
        if key not in range(self.size + 1):
            self.size = key + 1

        if value:
            self.storage[key] = value


    def __delitem__(self, key):
        """
        Delete an item from the array if it exists.
        """
        if key <= self.size:
            if key in self.storage.keys():
                del self.storage[key]
            self.size -= 1
        else:
            raise IndexError("Index not found")


    @property
    def print_non_zero(self):
        """
        Print only the key, value pairs where the value is not 0
        """
        for key, value in self.storage.items():
            print("index: {} => {}".format(key, value))


    @property
    def print_all(self):
        """
        Print the entire array including 0 value entries.
        """
        for index in range(self.size):
            try:
                if self.storage[index]:
                    print("index: {} => {}".format(index, self.storage[index]))
            except KeyError:
                print("index: {} => {}".format(index, 0))
