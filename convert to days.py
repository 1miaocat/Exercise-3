# Exercise 1

hours_per_day = 24
min_per_day = 1440
sec_per_day = 86400

def convert_to_days():
    hours = int(input('Enter number of hours: '))
    minutes = int(input('Enter number of minutes: '))
    seconds = int(input('Enter number of seconds: '))
    return get_days(hours, minutes, seconds)


def get_days(hours, minutes, seconds):
    days_from_hours = hours / hours_per_day
    days_from_minutes = minutes / min_per_day
    days_from_seconds = seconds / sec_per_day
    total_day = float(days_from_seconds + days_from_minutes + days_from_hours)
    return round(total_day, 4)

print('The number of days is: ',convert_to_days())
