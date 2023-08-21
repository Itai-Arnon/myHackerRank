def timeConversion(s):
    # Write your code here
    idx = s.find('M')
    am_pm = s[idx - 1:]
    time = s[:idx - 1]
    time = time.split(':')
    time = [int(x) for x in time]

    if am_pm == 'AM' and time[0] == 12:
        add = -12

    elif am_pm == 'AM':
        add = 0
    elif am_pm == 'PM' and time[0] == 12:
        add = 0
    else:
        add = 12

    time[0] = time[0] + add

    string = '{:02d}:{:02d}:{:02d}'.format(time[0], time[1], time[2])

    return string
