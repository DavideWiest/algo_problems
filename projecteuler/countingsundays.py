
START = 1901
monthsWith30Days = (4, 6, 9, 11)

isCentury = lambda year: (START+year) % 100 == 0
notDivisibleBy400 = lambda year: (START+year) % 400 != 0
isLeapYear = lambda year: (START+year) % 4 == 0 and \
    (False if isCentury(year) and notDivisibleBy400(year) else True)
determineDaysOfMonth = lambda month, year: \
    ((30 if month in monthsWith30Days else 31) if month != 2 else (28 if not isLeapYear(year) else 29))
sumUntil = lambda aList, i: sum(aList[:i])

month_days = [
    determineDaysOfMonth(month+1, year+1)
    for month in range(12)
    for year in range(100)
]
sundays_firstdays = sum([
    1
    for i in range(len(month_days))
    if (sumUntil(month_days, i)+1) % 7 == 0
])
print(sundays_firstdays)