temp_readings = [24.5, 24.8, 25.1, 25.0, 24.9]
print(temp_readings[2])

for temp in temp_readings:
  if temp > 25.0:
    print(f'High Temp Alert: {temp}°C')

#°

machine_id = ["1AVI1805", "1AVI1811", "1AVI0225", "1AVI0244"]
for machine in machine_id:
  print(f'Machine ID: {machine}')

def check_temp(temperature, min_temp=20.0, max_temp=26.0):
  if temperature < min_temp or temperature > max_temp:
    print("Not safe")
  else:
    print("good to go")

temps1 = temp_readings[0]
temps2 = temp_readings[2]
check_temp(temps1)

machine_temps = {"1AVI1805": 19, "1AVI1811": 24.8, "1AVI0225": 40, "1AVI0244": 25.0}

for machine, temp in machine_temps.items():
  status = check_temp(temp)
  print(f"Machine {machine} temperature is {temp}°C, status: {status}")
