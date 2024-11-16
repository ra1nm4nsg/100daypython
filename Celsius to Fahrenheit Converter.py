#user input temperature in celsius
temp_input = input("What is the temperature today in celsius? ")

#convert user input to fahrenheit
celsius_conv = (int(temp_input))
fahrenheit = (celsius_conv*(9/5)+32)
print("The tempareture converted to fahrenheit is", fahrenheit)