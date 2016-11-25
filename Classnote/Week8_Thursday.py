# Python 3 Iterator
import numpy as np


class Reverse:
    def __init__(self, data):
        """

        :param data:
        """
        self.index = len(data) # get the last index of data
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index ==0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5, 6]
    test = Reverse(a_list)
    # List comprehension
    print(list([i for i in test]))

    a_string = "the quick brown fox jumps over the lazy dog"
    print("".join([s for s in Reverse(a_string)]))

# Create a rank 2 Array using numPy
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(a[0, 0], a[1, 0])


