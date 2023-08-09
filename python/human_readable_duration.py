"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

~format_duration(62)    # returns "1 minute and 2 seconds"~
~format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"~

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated by
a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last
component, which is separated by " and ", just like it would be written in
English.

A more significant units of time will occur before than a least significant one.
 Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1
minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function
should not return 61 seconds, but 1 minute and 1 second instead. Formally, the
duration specified by of a component must not be greater than any valid more
significant unit of time.
"""

def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_periods = {'year': 31536000, 'day': 86400,
               'hour': 3600, 'minute': 60,
               'second': 1}

    period_counts = {}
    remainder = seconds
    for period in time_periods:
        if seconds >= time_periods[period]:
            count = remainder // time_periods[period]
            remainder = remainder - count * time_periods[period]
            if count != 0:
                period_counts[period] = count


    if len(period_counts) == 1:
        for period in period_counts:
            if period_counts[period] > 1:
                return f"{period_counts[period]} {period}s"
            else:
                return f"{period_counts[period]} {period}"

    else:
        formatted_str = ""
        for period in period_counts:
            if period == list(period_counts.keys())[-1]:
                if period_counts[period] > 1:
                    formatted_str = f"{formatted_str}and {period_counts[period]} {period}s"
                else:
                    formatted_str = f"{formatted_str}and {period_counts[period]} {period}"

            elif period == list(period_counts.keys())[-2]:
                if period_counts[period] > 1:
                    formatted_str = f"{formatted_str}{period_counts[period]} {period}s "
                else:
                    formatted_str = f"{formatted_str}{period_counts[period]} {period} "

            else:
                if period_counts[period] > 1:
                    formatted_str = f"{formatted_str}{period_counts[period]} {period}s, "
                else:
                    formatted_str = f"{formatted_str}{period_counts[period]} {period}, "


    return formatted_str

def main():
    helper = (
        f"Input a period of time in seconds. The function will return a string "
        f"formatted to represent the time in words, descending from 'year'. "
        f"The duration unitrepresented by the returned string is never greater "
        f"than what is passed in seconds (passing '60' will not return 0 "
        f"years, 0 days, 0 hours, 1 minute, and 0 seconds)."
        )

    seconds = int(input())
    print(format_duration(seconds))

if __name__ == '__main__':
    main()
