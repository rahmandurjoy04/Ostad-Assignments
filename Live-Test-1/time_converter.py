def hour_to_minute(hour):
    whole_hour = int(hour)
    whole_hour_in_minute =whole_hour *60
    fraction_hour = hour-whole_hour
    fraction_hour_in_minute = fraction_hour*60
    total_minute = whole_hour_in_minute+fraction_hour_in_minute
    return (total_minute)

time = hour_to_minute(1.1)
print("The converted time in minute is ",time)
