""" A quiz.
    Usage: python task.py <filename>.

    Use 'python tests.py' to run tests.
"""
import sys
import re


def normalize_date(year, month, day):
    """ Normalize and validate the date's entities """
    # Validate the day and month
    valid_range = 0 < day < 32 and 0 < month < 13
    valid_none_odd_day = (not month % 2 and day < 31 and month < 8) and \
                         (month % 2 and day < 31 and month > 7)
    valid_leap_month = day < 30 and month == 2
    if not valid_range and not valid_none_odd_day and not valid_leap_month:
        raise ValueError('Days and months have an illigal range')
    # Validate the year
    year = int("20{0:02}".format(year)) if year < 100 else year
    # Check off for a leap year
    if day == 29 and month == 2:
        #import ipdb; ipdb.set_trace()
        if not (not year % 4 and year % 100 and year % 400):
            # The year is NOT leap
            raise ValueError("Year is not valid")
    return year, month, day

def get_earliest_date(line):
    """ Gets earliest possible legal date between Jan 1, 2000 and Dec 31, 2999
        from the line."""
    error_msg = "{0} is illegal"
    dates = []
    matched = re.match(r'(\d{1,2}|\d{4})/(\d{1,2}|\d{4})/(\d{1,2}|\d{4})', line)
    if not matched:
        raise ValueError(error_msg.format(line))
    # Validate numbers
    numbers = [int(n) for n in matched.groups()]
    numbers = sorted([n for n in numbers if n >= 0 and n < 3000])
    is_valid = len(numbers) == 3 and numbers[1] < 100
    if not is_valid:
        raise ValueError(error_msg.format(line))
    numbers = sorted(numbers)
    # Rotate the list three times
    for i in range(3):
        try:
            dates.append(normalize_date(*numbers))
        except ValueError as msg:
            pass
        finally:
            numbers = numbers[1:] + numbers[:1]
    if not dates:
        raise ValueError(error_msg.format(line))
    return "{0}-{1}-{2}".format(*min(dates))


if __name__ == '__main__':
    earliest_date = ''
    try:
        with open(sys.argv[1]) as file:
            rline = file.readline().rstrip()
            earliest_date = get_earliest_date(rline)
    except IndexError:
        print "Error: Assumed to get the name of file as the argument."
        print ("Usage: python %s <filename>" % sys.argv[0])
    except ValueError  as msg:
        print("%s" % msg)
    else:
        print(earliest_date)
