# Task 5.4

raw_date =(input("What is the shorthand date today?" + '\n'))
day, month, year = int(raw_date[:2]), int(raw_date[3:5]), int(raw_date[6:10])

day = day + 1
if day == 32:
    day = "01"
    month = month + 1
else:
    next
if day == 31:
    day = "01"
    month = month + 1
    if day == 30: #and ( month[4] == 4 or month[4] == 6 or month[4] == 9 or month[:5] == 11):
        day = "01"
        month = month + 1
if month == 12 and day == 32:
    day = "01"
    month = "01"
    year = year + 1


day = str(day)
month = str(month)
year = str(year)

print(day + "/" + month + "/" + year)
