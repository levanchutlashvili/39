# test_numb3rs.py
import numb3rs

def test_validate_valid_ip():
    assert numb3rs.validate("192.168.0.1") == True

def test_validate_invalid_ip():
    assert numb3rs.validate("275.3.6.28") == False

def test_validate_zero_padding():
    assert numb3rs.validate("010.020.030.040") == True

def test_validate_leading_zero():
    assert numb3rs.validate("192.168.01.01") == True
