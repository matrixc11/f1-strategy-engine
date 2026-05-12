driver_name = "Charles Leclerc"
race_number = 16
lap_time = 81.643

print(driver_name)
print(type(lap_time))



#BLOCK 2

lap_times = [81.6, 82.1, 81.9, 83.4, 81.2, 84.0]

print(lap_times[0])
print(lap_times[-1])
print(len(lap_times))

lap_times.append(80.9)
print(lap_times)

fastest = min(lap_times)
print(f"fastest lap: {fastest} seconds")


#BLOCK 3

driver = { "name": "Lando Norris", "team": "Mclaren", "number":4, "points": 189
          }
print(driver["name"])
print(driver["team"])
      
driver["points"] = 206
print(driver["points"])
print(driver.keys())


#BLOCK 4

drivers = ["Verstappen", "Norris", "Leclerc", "Piastri", "Sainz"]
for driver in drivers:
    print(f"Driver: {driver}")

lap_times = [81.6, 82.1, 81.9, 83.4, 81.2]
for i, time in enumerate(lap_times):
    print(f"Lap{i+1}: {time} seconds")


#BLOCK 5

def seconds_to_laptime(seconds):
    minutes = int(seconds//60)
    remaining = round(seconds % 60,3)
    return f"{minutes}:{remaining:06.3f}"

print(seconds_to_laptime(81.643))
print(seconds_to_laptime(75.1))
print(seconds_to_laptime(103.456))