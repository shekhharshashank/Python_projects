def weather(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:
        return "Cold"

user_input=input("Enter The Temp:")
print(weather(float(user_input)))