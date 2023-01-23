# Task 5.3

runAgain = "yes"
while (runAgain == "yes"):
    # Getting time from user
    raw_time = str(input("Please enter the time in the 24 hour format (xx:xx:xx)"))

    # String Splitting the time
    hours, minutes, seconds = int(raw_time[:2]), int(raw_time[3:5]), int(raw_time[6:8])

    # If statementrs
    seconds = seconds + 1
    if seconds == 60:
        seconds = "00"
        minutes = minutes + 1
    if minutes == 60:
        minutes = "00"
        hours = hours + 1
    if hours == 24:
        seonds = "00"
        minutes = "00"
        hours = "00"


    print("%02d %02d %02d" % (hours, minutes, seconds))
    runAgain = input("Type yes to start again or no to exit" + '\n')
    
