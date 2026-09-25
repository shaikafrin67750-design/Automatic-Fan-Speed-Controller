# Automatic Fan Speed Controller
# Temperature based fan speed control

temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
    speed = 0
    print("Fan OFF")
elif temperature < 25:
    speed = 30
    print("Fan Speed: 30%")
elif temperature < 30:
    speed = 50
    print("Fan Speed: 50%")
elif temperature < 35:
    speed = 75
    print("Fan Speed: 75%")
else:
    speed = 100
    print("Fan Speed: 100%")

print("Temperature:", temperature, "°C")
print("Fan Speed:", speed, "%")