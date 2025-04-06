celcius_temps = [15, 0, 23, 3, -273]

fahrenheit_temps = list(map(lambda c: c *9/5 + 32, celcius_temps))

print('celcius', celcius_temps)
print('fahrenheit', fahrenheit_temps)
