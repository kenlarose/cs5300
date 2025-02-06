import pytest

import task1
# import task2
import task3


def test_task1_hello_world(capsys):
    task1.say_hello()
    captured_stout = capsys.readouterr()

    assert captured_stout.out.strip() == "Hello, World!"


def test_task3_number_signs():
    with pytest.raises(TypeError):
        task3.get_number_sign("wrong type")

    assert task3.get_number_sign(10) == "positive"
    assert task3.get_number_sign(-5) == "negative"
    assert task3.get_number_sign(0.0) == "unsigned"


def test_task3_first_ten_primes():
    primes = task3.first_ten_prime_numbers()
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_task3_sum_numbers():
    with pytest.raises(TypeError):
        task3.gauss_sum(3.14)

    assert task3.gauss_sum(100) == 5050
        