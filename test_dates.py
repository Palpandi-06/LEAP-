from dates import is_leap_year


def test_regular_leap():
    assert is_leap_year(2024)


def test_century_not_leap():
    assert not is_leap_year(1900)


def test_400_year_is_leap():
    assert is_leap_year(2000)


def test_common_year():
    assert not is_leap_year(2023)
