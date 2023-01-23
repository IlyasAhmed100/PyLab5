# Task 5.2

# Asking user to input the date
runAgain = "yes"
while (runAgain == "yes"):
    raw_date =(input("What is the shorthand date today?" + '\n'))
    day, month, year = raw_date[:2], raw_date[3:5], raw_date[6:10]
    actual_day = 0
    actual_month = ""
    actual_year = 0
    # Day Calculation 
    if day == "01":
        actual_day = (day[1] + "st")
        if day == "21" or day == "31":
            actual_day = (day[:2] + "st")
    elif day == "02":
        actual_day = (day[1] + "nd")
        if day == "22":
           actual_day = (day[:2] + "nd")
    elif day == "03":
       actual_day = (day[1] + "rd")
       if day == "23":
            actual_day = (day[:2] + "rd")
    elif day == "04" or day == "05" or day == "06" or day == "07" or day == "08" or day == "09":
        actual_day = (day[1] + "th")
    else:
        actual_day = (day[:2] + "th")

    # Month Calculation
    if month == "01":
        actual_month = "January"
    elif month == "02":
        actual_month = "February"
    elif month == "03":
        actual_month = "March"
    elif month == "04":
        actual_month = "April"
    elif month == "05":
        actual_month = "May"
    elif month == "06":
        actual_month = "June"
    elif month == "07":
        actual_month = "July"
    elif month == "08":
        actual_month = "August"
    elif month == "09":
        actual_month = "September"
    elif month == "10":
        actual_month = "October"
    elif month == "11":
        actual_month = "November"
    elif month == "12":
        actual_month = "December"

    # Year Calculation
    actual_year = year

    # Final Ouput

    print(actual_day, actual_month, actual_year)

    runAgain = input("Type yes to start again or no to exit" + '\n')
    
    
        
        

            
        
        




        
