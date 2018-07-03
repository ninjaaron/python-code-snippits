#  === Dating advice ===  #
MONTHS = {m: i+1 for i, m in enumerate(
    'jan feb mar apr may jun jul aug sep oct nov dec'.split()
)}


class BadDate(Exception):
    pass


def parse_date(string):
    """Parse a date with a four-digit year and the monthe spelled out or
    abbreviated. returns a tuple of ints, (year, month, day)
    """
    year, month, day = None, None, None
    for field in string.split():
        try:
            val = int(field.rstrip(','))
            if val > 31:
                year = val
            else:
                day = val
        except ValueError:
            month = MONTHS[field[0:3].lower()]

    if not all((year, month, day)):
        raise BadDate((year, month, day))

    return year, month, day
