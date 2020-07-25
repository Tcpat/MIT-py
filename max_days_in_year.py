from datetime import date, timedelta

def most_frequent_days(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    delta = (timedelta(days = 1))
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dict_days = {}
    for day in week_days:
        dict_days[day] = 0
    while start_date <= end_date:
        day = start_date.weekday()
        dict_days[week_days[day]] += 1
        start_date += delta
    number_days = dict_days.values()
    max_number = max(number_days)
    max_days = []
    for i in dict_days:
        if dict_days[i] == max_number:
            max_days.append(i)
    return max_days
