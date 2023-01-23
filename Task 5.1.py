# Task 5.1
print("Enter the speed of wind and we will bring out the relevant output from the Beaufort Scale")

# Getting the wind speed from user
wind_speed = int(input("How fast is the wind?"))

# Getting relevant outputd from Beaufort Scale
if wind_speed < 1:
    print("Calm")
elif 1<= wind_speed < 12:
    print("Gentle Breeze")
elif 12<= wind_speed < 30:
    print("Strong Breeze")
elif 30<= wind_speed < 46:
    print("Gale")
elif 46<= wind_speed < 63:
    print("Storm")
elif 63 <= wind_speed < 74:
    print("Violent Storm")
else:
    print("Hurricane Force")
