def is_leap_year(year):
    """Gregorian leap-year rule."""
    return year % 4 == 0 and year % 100 != 0
