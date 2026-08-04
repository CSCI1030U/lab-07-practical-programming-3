from lab07 import count_occurrences, is_sorted, Rectangle, Square


def test_count_occurrences():
    assert count_occurrences(2, [1, 2, 2, 3, 2]) == 3
    assert count_occurrences(5, [1, 2, 3]) == 0
    assert count_occurrences(1, []) == 0
    assert count_occurrences("a", ["a", "b", "a"]) == 2


def test_is_sorted():
    assert is_sorted([1, 2, 3])
    assert not is_sorted([1, 3, 2])
    assert is_sorted([])
    assert is_sorted([5])
    assert is_sorted([2, 2, 3])
    assert not is_sorted([3, 1])


def test_rectangle():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14
    assert str(r) == "3x4"


# STRETCH (optional) - skipping the Square still passes the three parts above.
def test_square():
    s = Square(5)
    assert s.area() == 25
    assert s.perimeter() == 20
    assert str(s) == "5x5"
    assert isinstance(s, Rectangle)
