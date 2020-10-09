# Exercise 5

def convert_temp():
    temp_f = int(input('Enter temerature in Fahrenheit: '))
    print('The temperature in Fahrenheit is: ',temp_f)
    print('The temperature in Celcius is: ',convert_to_celcius(temp_f))
    print('The temperature in Kelvin is: ', convert_to_kelvin(convert_to_celcius(temp_f)))

def convert_to_celcius(temp_f):
    temp_c = (5/9) * (temp_f - 32)
    return temp_c

def convert_to_kelvin(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

print(convert_temp())
