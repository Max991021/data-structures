import pytest
from data_structures import (
    split_temperatures,
    build_product_index,
    normalize_unique_categories,
    group_students_by_course,
    chunk_transactions,
    invert_employee_manager_map,
    fibonacci_sequence
)


# ============================
# Question 1 Tests
# ============================
def test_split_temperatures_basic():
    data = [(10, 20), (15, 25), (18, 30)]
    assert split_temperatures(data) == ([10, 15, 18], [20, 25, 30])


def test_split_temperatures_empty():
    assert split_temperatures([]) == ([], [])


# ============================
# Question 2 Tests
# ============================
def test_build_product_index():
    products = ["Milk", "Bread", "Eggs"]
    assert build_product_index(products) == {
        "Milk": 0,
        "Bread": 1,
        "Eggs": 2
    }


# ============================
# Question 3 Tests
# ============================
def test_normalize_unique_categories():
    data = ["Tech", "tech", "FOOD", "Food"]
    assert normalize_unique_categories(data) == {"tech", "food"}


# ============================
# Question 4 Tests
# ============================
def test_group_students_by_course():
    students = [
        {"name": "Anna", "course": "Math"},
        {"name": "Ben", "course": "Math"},
        {"name": "Cara", "course": "Physics"}
    ]

    assert group_students_by_course(students) == {
        "Math": ["Anna", "Ben"],
        "Physics": ["Cara"]
    }


# ============================
# Question 5 Tests
# ============================
def test_chunk_transactions_default_size():
    data = ["T1", "T2", "T3", "T4"]
    assert chunk_transactions(data) == [
        ["T1", "T2", "T3"],
        ["T4"]
    ]


def test_chunk_transactions_custom_size():
    data = ["T1", "T2", "T3", "T4"]
    assert chunk_transactions(data, size=2) == [
        ["T1", "T2"],
        ["T3", "T4"]
    ]


def test_chunk_transactions_invalid_size():
    with pytest.raises(ValueError):
        chunk_transactions(["T1", "T2"], size=0)


# ============================
# Question 6 Tests
# ============================
def test_invert_employee_manager_map():
    data = {
        "Alice": "Manager1",
        "Bob": "Manager1",
        "Clara": "Manager2"
    }

    assert invert_employee_manager_map(data) == {
        "Manager1": ["Alice", "Bob"],
        "Manager2": ["Clara"]
    }


# ============================
# Question 7 Tests
# ============================
def test_fibonacci_sequence_basic():
    assert fibonacci_sequence(6) == [0, 1, 1, 2, 3, 5]


def test_fibonacci_sequence_zero():
    assert fibonacci_sequence(0) == []


def test_fibonacci_sequence_negative():
    with pytest.raises(ValueError):
        fibonacci_sequence(-3)
