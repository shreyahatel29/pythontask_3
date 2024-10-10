# Dictionary Methods

#1. The clear() method removes all the elements from a dictionary.

car = {
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2016
}

car.clear()

print(car)

# 2.The copy() method returns a copy of the specified dictionary.

car = {
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2016
}

result = car.copy()

print(result)

# 3.The fromkeys() method returns a dictionary with the specified keys and the specified value.

print()
x = ('s',2,5,True)
print(f'x={x}')
print()
x = dict.fromkeys(x, 8)

print(f'output_fromkeys :{x}')
print('---')

# 4. The get() method returns the value of the item with the specified key.

print()
car = {
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2016
}

result = car.get("model")

print(result)
print('---')

# 5. The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

print()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

result = car.items()

print(result)

# 6. The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
print('---')
numbers = {
    1:'one',
    2:'two',
    3:'three',
    4:'four'
}
print(f'numbers ={numbers}')
dictionaryKeys = numbers.keys()
print(dictionaryKeys)
print()

# 7. The pop() method removes the specified item from the dictionary.

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "Italy": "Rome"
}
print(f'country_capitals = {country_capitals}')
result = country_capitals.pop('Canada')
print('Popped_country:' , result)

# 8. The update() method inserts the specified items to the dictionary.

print()
car = {
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2016
}
print(f'car = {car}')

car.update({"color": "White"})

print(car)
print('---')

# 9. The popitem() method removes the item that was last inserted into the dictionary.

numbers = {
    1:'one',
    2:'two',
    3:'three',
    4:'four'
}
print(f'numbers ={numbers}')
numbers.popitem()
print(f'output_popitem:{numbers}')
print()

# 10. The setdefault() method returns the value of the item with the specified key.

users = {
    'u_id': 101,
    'Name': 'John',
    'Dept': 'DBA'

}
print(f'users = {users}')
print()
users.setdefault('Salary',13000)
print(f'output_setdefault:{users}')
print()

# 11. The values() method returns a list of all the values in the dictionary.

car = {
  "brand": "Hyundai",
  "model": "Creta",
  "year": 2016
}
print(f'car = {car}')
print()
x = car.values()
print(f'x = {x}')