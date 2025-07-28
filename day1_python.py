temp_readings = [24.5, 24.8, 25.1, 25.0, 24.9]
print(temp_readings[2])

for temp in temp_readings:
  if temp > 25.0:
    print(f'High Temp Alert: {temp}°C')
