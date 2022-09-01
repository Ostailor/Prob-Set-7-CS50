from Numb3rs.numb3rs import validate


def test_check_half():
    assert validate("220.200.243.2") == True
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
