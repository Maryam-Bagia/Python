# Activity - 2

temperature = {'Monday': 22, 'Tuesday': 28, 'Wednesday': 19, 'Thursday': 24, 'Friday': 30}

filtered_temp = {day: temp for day, temp in temperature.items() if 20 <= temp <= 25}
print(filtered_temp)

# Output:
# {'Monday': 22, 'Thursday': 24}



