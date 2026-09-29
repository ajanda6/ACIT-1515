def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

def getDayOfTheWeek(year, month, day):
    last_two_digits = year % 100

    num_of_twelves = last_two_digits // 12

    remainder = last_two_digits % 12

    num_of_fours = remainder // 4

    month_codes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    month_code = month_codes[month - 1]

    if isLeapYear(year) and (month == 1 or month == 2):
        month_code = month_code - 1

    century = year // 100

    if century == 16:
        month_code = month_code + 6
    elif century == 17:
        month_code = month_code + 4
    elif century == 18:
        month_code = month_code + 2
    elif century == 20:
        month_code = month_code + 6
    elif century == 21:
        month_code = month_code + 4


    total = num_of_twelves + remainder + num_of_fours + day + month_code

    day_number = total % 7

    days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

    return days[day_number]

def makeCalendar():
    year = 2026

    for month in range(1, 13):
        if month == 2:
            if isLeapYear(year):
                days_in_month = 29
            else:
                days_in_month = 28

        elif month == 4 or month == 6 or month == 9 or month == 11:
            days_in_month = 30

        else:
            days_in_month = 31

        for day in range(1, days_in_month + 1):
            day_of_week = getDayOfTheWeek(year, month, day)

            print(str(month) + "-" + str(day) + "-" + str(year) +
                  " is a " + day_of_week + ".")