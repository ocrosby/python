from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.offset = 0
        self.v1 = v1
        self.v2 = v2
        self.length1 = len(v1)
        self.length2 = len(v2)
        self.min_length = min(self.length1, self.length2)

    def next(self) -> int:
        """
        Returns the next element in the zigzag iteration
        :return:
        """

        # Check if the offset falls in the first part of the cycling through
        # both lists
        if self.offset < 2 * self.min_length:
            # The offset falls in the first part of cycling through both lists.
            if self.offset % 2 == 0:
                # The offset is even, get the next element from the first list.
                k = self.v1[self.offset // 2]
            else:
                # The offset is odd, get the next element from the second list.
                k = self.v2[self.offset // 2]
        else:
            # The offset falls in the second part completing the longer list.
            if self.length1 > self.length2:
                # The first list is longer than the second list.
                # get the next element from the tail of the first list based on the offset
                k = self.v1[self.offset - self.min_length]
            else:
                # The second list is longer than the first list.
                # get the next element from the tail of the second list based on the offset
                k = self.v2[self.offset - self.min_length]

        self.offset += 1

        return k

    def has_next(self) -> bool:
        """
        Returns True if there are additional elements in the zigzag iteration
        :return:
        """
        return self.offset < self.length1 + self.length2


if __name__ == "__main__":
    pass