seconds = int(input("Enter the amount of seconds: "))
minutes = seconds // 60
hours = minutes // 60
rem_seconds = seconds % 60
rem_minutes = minutes % 60
rem_hours = hours % 60
print(
    seconds,
    "seconds is",
    rem_hours,
    "hours",
    rem_minutes,
    "minutes",
    "and",
    rem_seconds,
    "seconds",
)
