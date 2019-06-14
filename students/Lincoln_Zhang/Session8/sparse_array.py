#!/usr/bin/env python3

class sparse_array:
    """
    This class is to take one dimentional array convert it to dictionary.
    it can tell the length of the array
    """

    def __init__(self,sample_array):
        self.sample_array = sample_array
    """
    this is a property function to get array length without instantiate the class

    """
    @property
    def array_length(self,sample_array):
        self.sample_arrary = sample_array
        return len(self.sample_arrary)
    """
    this is a static method to convert an array to a dictionary and ignore value 0

    """
    @staticmethod
    def SparseArray(sample_array):
        # self.sample_arrary = sample_array
        return {k:v for (k,v) in enumerate(sample_array)}



