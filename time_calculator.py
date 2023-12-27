def add_time(start, duration, day=None):
    am_pm = start.split(" ")[1]
    start_time = start.split(":")
    duration_time = duration.split(":")
    start_hours, start_minutes = start_time[0], start_time[1].split(" ")[0]
    duration_hours, duration_minutes = duration_time[0], duration_time[1]
    new_time = ""
    n_days = 0
    while int(duration_hours) >= 24:
        n_days += 1
        duration_hours = str(int(duration_hours) - 24)
    
    days_week = {
        "sunday":1,
        "monday":2,
        "tuesday":3,
        "wednesday":4,
        "thursday":5,
        "friday":6,
        "saturday":7
    }
    
    if day is not None:
        day_number = days_week.get(day.lower())
        total_days = n_days + day_number
        while total_days > 7:
            total_days -= 7

        for day, value in days_week.items():
             if total_days == value:
                 final_day = day.capitalize()
    
    if n_days == 0:
        days_later = ""
        
    if am_pm == "AM":  
        total_hours = str(int(start_hours) + int(duration_hours))
        total_minutes = str(int(start_minutes) + int(duration_minutes))
        if int(total_minutes) >= 60:
            total_minutes = str(int(total_minutes) - 60)
            total_hours = str(int(total_hours) + 1)
        if len(total_minutes) < 2:
            total_minutes = "0{}".format(total_minutes)
        if (int(total_hours) == 12) and (int(start_hours == 12)):
            new_time += "{}:{} AM".format(total_hours,total_minutes)
        elif (int(start_hours) == 12) and (int(total_hours) < 24):
            new_time += "{}:{} AM".format(int(total_hours)-12,total_minutes)
        elif int(total_hours) == 12:
            new_time = "12:{} PM".format(total_minutes)
        elif int(total_hours) < 12:
            new_time += "{}:{} AM".format(total_hours,total_minutes)
        else:
            new_time += "{}:{} PM".format((int(total_hours)-12),total_minutes)
        if n_days == 1:
            days_later =  " (next day)"
        elif n_days > 1:
            days_later = " ({} days later)".format(n_days)
    
    if am_pm == "PM":
        total_hours = str(int(start_hours) + int(duration_hours))
        total_minutes = str(int(start_minutes) + int(duration_minutes))
        if int(total_minutes) > 60:
            total_minutes = str(int(total_minutes) - 60)
            if len(total_minutes) < 2:
                total_minutes = "0{}".format(total_minutes)
            total_hours = str(int(total_hours) + 1)
        if (int(start_hours) == 12) and (int(total_hours) <= 12):
            new_time = "{}:{} PM".format(total_hours,total_minutes)
        elif (int(total_hours) == 12):
            new_time = "12:{} AM".format(total_minutes)
            new_day_number = days_week.get(final_day.lower()) + 1
            if new_day_number > 7:
                new_day_number -= 7
            for day,value in days_week.items():
                if new_day_number == value:
                    final_day = day.capitalize()
            n_days += 1
        elif (int(start_hours) == 12) and (int(total_hours) < 24):
            new_time += "{}:{} PM".format((int(total_hours)-12),total_minutes)
        elif int(total_hours) < 12:
            new_time += "{}:{} PM".format(total_hours,total_minutes)
        else:
            new_time += "{}:{} AM".format((int(total_hours)-12),total_minutes)
            n_days += 1
            new_day_number = days_week.get(final_day.lower()) + 1
            if new_day_number > 7:
                new_day_number -= 7
            for day,value in days_week.items():
                if new_day_number == value:
                    final_day = day.capitalize()
        if n_days == 1:
            days_later = " (next day)"
        elif n_days > 1:
            days_later = " ({} days later)".format(n_days)

    if day is not None:
        new_time = (new_time + "," + " " + final_day + days_later).rstrip()
    else:
        new_time = (new_time + " " + days_later).rstrip()
    return new_time

