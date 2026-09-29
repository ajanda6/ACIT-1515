import dow

def getDayOfTheWeekForUserDate():
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))
    year = int(input("Enter a year: "))

    day_of_week = dow.getDayOfTheWeek(year, month, day)

    print(str(month) + "-" + str(day) + "-" + str(year) + " is a " + day_of_week + ".")


dow.makeCalendar()

getDayOfTheWeekForUserDate()