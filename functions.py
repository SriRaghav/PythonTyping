# Type hinting python functions

# Python functions can also have type hints. The values it accepts and the values it returns can be annotated
# ahead of time using type hints


# No Type Hint
def format_weather_message(day, temperature):
    return "The weather on {} is {}".format(day, temperature)

print(format_weather_message("Monday", 70))


# With Type Hint
def format_weather_message_th(day: str, temperature: int) -> str:
    return "The weather on {} is {}".format(day, temperature)

print(format_weather_message_th("Monday", 70))


# find average temperature function call will work with a list or a dictionary and both are valid inputs
# but may not yield the same result

# No Type Hint
def find_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)


temperature_list = [68, 70, 72, 75, 70, 68, 65]
temperature_dict = {1: 68, 2: 70, 3: 72, 4: 75, 5: 70, 6: 68, 7: 65}

print(find_average_temperature(temperature_list))
print(find_average_temperature(temperature_dict))


# With Type Hint
def find_average_temperature_th(temperatures: list) -> float:
    return sum(temperatures) / len(temperatures)

print(find_average_temperature_th(temperature_list))
print(find_average_temperature_th(temperature_dict))


# https://testdriven.io/blog/python-type-checking/