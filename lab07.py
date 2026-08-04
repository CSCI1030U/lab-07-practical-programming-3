# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):
    # TODO (Part 1, recursion): return how many times `target` appears in the list
    #   `values`.
    #   Base case: an empty list contains it 0 times.
    #   Recursive case: 1 (if the first item equals `target`, otherwise 0) plus the
    #   count in the rest of the list, values[1:].
    pass


def is_sorted(values):
    # TODO (Part 2, recursion): return True if `values` is in non-decreasing order
    #   (every item is <= the one after it), otherwise False.
    #   Base case: a list of 0 or 1 items is already sorted.
    #   Recursive case: the first two items are in order AND the rest is sorted.
    pass


class Rectangle:
    def __init__(self, width, height):
        # TODO (Part 3, OOP): store width and height on self
        pass

    def area(self):
        # TODO: return width * height
        pass

    def perimeter(self):
        # TODO: return 2 * (width + height)
        pass

    def __str__(self):
        # TODO: return "<width>x<height>", e.g. Rectangle(3, 4) -> "3x4"
        pass


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        # TODO: a Square is a Rectangle whose width and height are the same. Call the
        #   Rectangle constructor with `side` for both (use super().__init__(...)).
        #   area, perimeter, and __str__ are then inherited automatically.
        pass


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    # print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    # print(is_sorted([1, 2, 3]))                    # True
    # print(Rectangle(3, 4).area())                  # 12
    # print(Square(5))                               # 5x5
    pass


if __name__ == "__main__":
    main()
