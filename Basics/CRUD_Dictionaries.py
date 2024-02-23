# CREATE 
foods = {"pizza": "2.50",
         "pasta": "6.00",
         "noodles": "3.50",
         "chicken rice": "5.00"}

# READ
print(foods.get("chicken rice"))
# use of if statement to check if key exists in dictionary 
if foods.get("chicken rice"):
  print("That food item is sold in this canteen")
else:
  print("That food item is not sold")

# UPDATING 
foods.update({"fried rice": "4.50"}) # adding a new key value pair 

foods.update({"chicken rice": "6.00"}) # changing value of existing key 

# DELETE 
foods.pop("pasta") # deleting a specific key 
foods.popitem() # deleting the latest key value pair added to the dictionary 

# READ (2.0)
keys = foods.keys() # retrieve all keys

for key in foods.keys(): # iterate through all keys 
  print(key)

values = foods.values() # retrieve all values

for value in foods.values(): # iterate through all values 
  print(value)

items = foods.items() # returns a dictionary object which resembles a 2d list of tuples

for key, value in foods.items(): # for loop with 2 counters 
  print(f"{key}: {value}") # use of f string 
