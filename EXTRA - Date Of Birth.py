import calendar, time

today = print('Today is', time.ctime(), '\n')

valid = False
while not valid:
    m = input('Enter your birthmonth(1-12): ')
    if not m.isnumeric():
        print("Please enter a number between 1-12.")
    else:
        m = int(m)
        if m <= 0 or m > 12:
            print("Please enter a number between 1-12")
        else:
            break

while not valid:
    d = input('Enter your date of Birthday (1-31): ')
    if not d.isnumeric():
        print("Please enter a number between 1-31.")
    else:
        d = int(d)
        if d <= 0 or d > 31:
            print("Please enter a number between 1-31")
        else:
            valid = True

while True:
    try:
        y = int(input('Enter your birthyear: '))
    except ValueError:
        continue
    if y < 1000 or y > 2021:
        continue
    else:
        break

print(f'\nYour birthday is {m}.{d}.{y}')

wd = calendar.weekday(y, m, d)

print('It was', calendar.day_name[wd], 'that day. \n')

print('Here is the month calendar of your birthday:\n', calendar.month(y, m))