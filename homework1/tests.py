import pytest

import task1
# import task2
import task3
import task4


def test_task1_hello_world(capsys):
    """captures standard output to validate the function prints "Hello, World!"""
    task1.say_hello()
    captured_stout = capsys.readouterr()

    assert captured_stout.out.strip() == "Hello, World!"


def test_task3_number_signs():
    assert task3.get_number_sign(10) == "positive"
    assert task3.get_number_sign(-5) == "negative"
    assert task3.get_number_sign(0.0) == "unsigned"


def test_task3_first_ten_primes():
    primes = task3.first_ten_prime_numbers()
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_task3_sum_numbers():
    """validates the function correctly sums all integers from 1 to 100,
       and that the function only accepts integer args"""
    with pytest.raises(TypeError):
        task3.gauss_sum(3.14)

    assert task3.gauss_sum(100) == 5050
        

def test_task4_calculate_discount():
    """validates args are within the bounds of price-discount relationship, 
       and that the returned value type is float unless both args are int"""
    with pytest.raises(ValueError):
        task4.calculate_discount(-4.44, 2)
    with pytest.raises(ValueError):
        task4.calculate_discount(12.50, 13)

    assert isinstance(task4.calculate_discount(10, 3), int)
    assert isinstance(task4.calculate_discount(10.00, 3), float)
    assert isinstance(task4.calculate_discount(10, 2.99), float)
    assert isinstance(task4.calculate_discount(10.00, 2.99), float)

