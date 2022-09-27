#!/usr/bin/python
import pytest


@pytest.fixture()
def before_method():
    print("\n------setup-------\n")
    yield
    print("\n------teardown------\n")


def get_title(keyValue):
    """get the value for the title key"""
    # print("\nTitle: {} ".format(dictionary['Title']))
    title = keyValue['Title']
    return title


def check_title(title):
    """check title is a valid output
    Valid types are explicitly ['Mr', 'Mrs', 'Ms'].
    These are also case-sensitive.
    These are of type string"""

    if type(title) == str:
        if not (len(title.strip())):  # raises exception for empty string
            raise TypeError(
                'Title ({}) : was an empty string : {}. Length of string should not be null'.format(title, type(title)))
        if title.islower() or title.isupper():  # raises exception for lower and upper case titles
            raise TypeError('Title : ({}) is case-sensitive. Title should be a <Proper> Case'.format(title))
        elif title not in ['Mr', 'Mrs', 'Ms']:
            raise TypeError('Title : ({}) is invalid. Valid titles are :  "Mr", "Mrs","Ms"'.format(title))

    if type(title) != str:  # raises exception for non-string titles
        raise TypeError('Title : ({}) is NOT a string {}. Title should be a string.'.format(title, type(title)))
    if not (len(title.strip())):  # raises exception for empty titles
        raise TypeError(
            'Title passed was an empty string : {}. Length of string should not be null'.format(type(title)))


def getGender(title):
    """takes a title as a parameter and returns gender as male or female"""
    # print(title)

    if title == 'Mrs' or title == 'Ms':
        gender = "female"
    else:
        gender = 'male'

    # print("\nTitle: {} returns Gender: {}".format(title, gender))
    return gender


# -------------------------POSITIVE CASES-------------------------
def test_for_mr_title():
    data = {'User_id': '1342567893', 'Title': 'Mr', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    expected_title = 'Mr'
    actual_title = get_title(data)
    assert actual_title == expected_title


def test_for_mrs_title():
    data = {'User_id': '1342567893', 'Title': 'Mrs', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    expected_title = 'Mrs'
    actual_title = get_title(data)
    assert actual_title == expected_title


def test_for_ms_title():
    data = {'User_id': '1342567893', 'Title': 'Ms', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    expected_title = 'Ms'
    actual_title = get_title(data)
    assert actual_title == expected_title


def test_return_male_with_mr_title():
    data = {'User_id': '1342567893', 'Title': 'Mr', 'Age': '1001', 'Monthly_number_of_hours_watched': 0}
    title = get_title(data)
    gender = getGender(title)
    return gender


def test_return_female_with_mrs_title():
    data = {'User_id': '1342567893', 'Title': 'Mrs', 'Age': '1001', 'Monthly_number_of_hours_watched': 0}
    title = get_title(data)
    gender = getGender(title)
    return gender


def test_return_female_with_ms_title():
    data = {'User_id': '1342567893', 'Title': 'Ms', 'Age': '1001', 'Monthly_number_of_hours_watched': 0}
    title = get_title(data)
    check_title(title)
    gender = getGender(title)
    return gender


# -------------------------NEGATIVE CASES-------------------------

def test_with_number_as_title():
    data = {'User_id': '1342567893', 'Title': 5, 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_no_title():
    data = {'User_id': '1342567893', 'Title': None, 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_empty_string_for_title():
    data = {'User_id': '1342567893', 'Title': '', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_whitespace_for_string_title():
    data = {'User_id': '1342567893', 'Title': '    ', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_string_with_spaces():
    data = {'User_id': '1342567893', 'Title': 'Mrs  ', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_lowercase_title():
    data = {'User_id': '1342567893', 'Title': 'mrs', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_uppercase_title():
    data = {'User_id': '1342567893', 'Title': 'MS', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_invalid_title():
    data = {'User_id': '1342567893', 'Title': 'Dr', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)


def test_with_special_character_as_title():
    data = {'User_id': '1342567893', 'Title': '@', 'Age': '52', 'Monthly_number_of_hours_watched': 856.47}
    title = get_title(data)
    check_title(title)
