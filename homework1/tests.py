import pytest
import os
import glob

import task1
import task2
import task3
import task4
import task5
import task6
import task7

# task 1
def test_task1_hello_world(capsys):
    """captures standard output to validate the function prints "Hello, World!"""
    task1.say_hello()
    captured_stout = capsys.readouterr()

    assert captured_stout.out.strip() == "Hello, World!"


# task 2
def test_task2_integer_operations():
    """integers can perform basic arithmetic"""
    assert task2.add(2, 3) == 5
    assert task2.subtract(10, 8) == 2
    assert task2.multiply(10, 2) == 20
    
    # standard division returns a float...
    expected_float = task2.standard_divide(20, 4)
    assert isinstance(expected_float, float)
    assert expected_float == 5.0

    # ...so you may want to use floor division if you want int
    expected_int = task2.floor_divide(20, 4)
    assert isinstance(expected_int, int)
    assert expected_int == 5

def test_task2_float_operations():
    """floats can perform basic arithmetic with decimals"""
    assert task2.add(3.14, 6.86) == 10.0
    assert task2.subtract(4.5, 2.3) == 2.2
    assert task2.multiply(10.0, 0.5) == 5.0

    # be careful with precision of floating point numbers
    imprecise_quotient = task2.standard_divide(10.0, 3.0)
    assert imprecise_quotient == 3.3333333333333335
    assert imprecise_quotient == pytest.approx(3.33333333333333)

    # if any operands for floor division are float,
    # then the statement will evaluate to float
    quotient = task2.floor_divide(10.0, 3)
    assert isinstance(quotient, float)
    assert quotient == 3.0

def test_task2_string_operations():
    """demonstrates a small sample of string operations"""
    assert task2.concatenate("Howdy, ", "Partner!") == "Howdy, Partner!"

    assert task2.find_index_of("Howdy, Partner!", "Par") == 7
    assert task2.find_index_of("Howdy, Partner!", "notthere") == -1

    assert task2.get_slice("Howdy, Partner!", 0, 5) == "Howdy"
    assert task2.get_slice("Howdy, Partner!", 7, 14) == "Partner"
 
    # demonstrating the use of optional parameters (default value None)
    assert task2.split_string("Howdy, Partner!") == ["Howdy,", "Partner!"]
    assert task2.split_string("Howdy, Partner!", ",") == ["Howdy", " Partner!"]

def test_task2_bool_operations():
    assert task2.logical_and(True, True) == True
    assert task2.logical_and(True, False) == False
    assert task2.logical_and(False, True) == False
    assert task2.logical_and(False, False) == False

    assert task2.logical_or(True, True) == True
    assert task2.logical_or(True, False) == True
    assert task2.logical_or(False, True) == True
    assert task2.logical_or(False, False) == False

    assert task2.logical_xor(True, True) == False
    assert task2.logical_xor(True, False) == True
    assert task2.logical_xor(False, True) == True
    assert task2.logical_xor(False, False) == False

    assert task2.logical_not(True) == False
    assert task2.logical_not(False) == True


# task 3
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
        

# task 4
def test_task4_calculate_discount():
    # function validates args are within the bounds of price-discount relationship
    with pytest.raises(ValueError):
        task4.calculate_discount(-4.44, 2)
    with pytest.raises(ValueError):
        task4.calculate_discount(12.50, 13)

    assert isinstance(task4.calculate_discount(10, 3), int)
    assert isinstance(task4.calculate_discount(10.00, 3), float)
    assert isinstance(task4.calculate_discount(10, 2.99), float)
    assert isinstance(task4.calculate_discount(10.00, 2.99), float)


# task 5
def test_task5_get_first_three_books():
    first_three_books = task5.get_first_three_favorite_books()
    assert len(first_three_books) == 3
    assert first_three_books == ["A Scanner Darkly", "House of Leaves", "Blood Meridian"]


def test_task5_get_students(): 
    students = task5.get_students()
    assert len(students) == 5
    
    for key, value in students.items():
        assert isinstance(key, str)
        assert key in ["Philip", "Mark", "Cormack", "Hermann", "Seneca"]
        assert isinstance(value, int)
        assert value in [12345, 67890, 58372, 83475, 87374]


# task 6
task6_expected_word_counts = {
    "task6_read_me.txt": 104,
    "task6_read_me_short_14.txt": 14,
    "task6_read_me_long_178.txt": 178,
}

def get_txt_files():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    txt_files = glob.glob(os.path.join(project_dir, "./*.txt"))
    return [os.path.basename(path) for path in txt_files]

def test_task6_word_count(word_count_filename):
    word_count = task6.get_file_word_count(word_count_filename)

    # assert word count match on prepared test files
    if word_count_filename in task6_expected_word_counts.keys():
        assert task6_expected_word_counts[word_count_filename] == word_count
    else:
        assert word_count > 0

def pytest_generate_tests(metafunc):
    """
    dynamically generates test cases based on param 'word_count_filename'

    Code developed with assistance from Claude (version 3.5 Sonnet), 
    an AI assistant created by Anthropic (consulted February 2025)
    """
    if "word_count_filename" in metafunc.fixturenames:
        txt_files = get_txt_files()
        metafunc.parametrize("word_count_filename", txt_files)


# task 7
def test_task7_reshape_array():
    """validate reshaping a one dimensional array to a
       two dimensional array using numpy"""
    array = task7.new_one_dimensional_array(9)
    original_attributes = task7.get_array_attributes(array)

    assert original_attributes["dimensions"] == 1
    assert original_attributes["size"] == 9
    assert original_attributes["shape"] == (9,)

    reshaped = task7.reshape_to_two_dimensions(array)
    reshaped_attributes = task7.get_array_attributes(reshaped)

    assert reshaped_attributes["dimensions"] == 2
    assert reshaped_attributes["size"] == 9
    assert reshaped_attributes["shape"] == (3, 3)
