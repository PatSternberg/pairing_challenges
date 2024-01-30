import pytest
from lib.age_checker import *

# As an admin
# So that I can determine whether a user is old enough
# I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.
# No test for this

# As an admin
# So that under-age users can be denied entry
# I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).
def test_underage():
    assert age_checker('2023-01-01') == 'You are 1 and are required to be 16 - access denied!'

# As an admin
# So that old enough users can be granted access
# I want to send a message to any user aged 16 or older to say that access has been granted.
def test_of_age():
    assert age_checker('1950-01-01') == 'Access granted - you are 74!'

def test_zero():
    assert age_checker('2024-01-01') == 'You are 0 and are required to be 16 - access denied!'

def test_months():
    assert age_checker('2009-02-01') == 'You are 15 and are required to be 16 - access denied!'

# As an admin
# So that invalid entries are rejected
# I want to generate an exception when the date of birth isn't the right type or format.
def test_exception_format():
    with pytest.raises(Exception) as e:
        age_checker('Banana')
    error_message = str(e.value)
    assert error_message == 'Wrong format'

def test_exception_type():
    with pytest.raises(Exception) as e:
        age_checker(25)
    error_message = str(e.value)
    assert error_message == 'Wrong type'