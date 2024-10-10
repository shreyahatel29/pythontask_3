# List Methods

# 1. The append() method appends an element to the end of the list.

fruits = ['apple', 'banana', 'cherry']
print(f'fruits = {fruits}')
print()
fruits.append("orange")
print('orange is appended :',fruits)

# 2. The clear() method removes all the elements from a list.

print('---')
fruits = ['apple', 'banana', 'cherry', 'orange']
print(f'fruits = {fruits}')
print()
fruits.clear()
print('output after applying clear(): ',fruits)
print('---')

# 3. The copy() method returns a copy of the specified list.

colors = ['Red','Black','White','Pink']
print(f'colors = {colors}')
print()
colors.copy()
print('output after applying copy() method: ',colors)
print('---')

# 4. The count() method returns the number of elements with the specified value.

colors = ['Red','Black','White','Pink']
print(f'colors = {colors}')
print()
x = colors.count('Black')
print(f'x = {x}')
print('---')

# 5. The extend() method adds the specified list elements (or any iterable) to the end of the current list.

cars = ['Ford', 'BMW', 'Creta']
print(f'cars = {cars}')
colors = ['Red','White','Black']
print(f'colors = {colors}')
print()
cars.extend(colors)
print('output after extend: ', cars)
print('---')

# 6. The index() method returns the position at the first occurrence of the specified value.

vegies = ['Spinach','Cabbage','Cauliflower']
print(f'vegies = {vegies}')
print()
result = vegies.index('Cabbage')
print('Index of Cabbage: ',result)
print('---')

# 7. The insert() method inserts the specified value at the specified position.

subjects = ['Chemistry','Physics','Maths']
print(f'subjects = {subjects}')
print()
subjects.insert(2,'Biology')
print('output after insertion: ',subjects)
print('---')

# 8. The pop() method removes the element at the specified position.

vegies = ['Spinach','Cabbage','Cauliflower']
print(f'vegies = {vegies}')
print()
x = vegies.pop(1)
print(f'vegies = {vegies}')
print('---')

# 9. The remove() method removes the first occurrence of the element with the specified value.

subjects = ['Chemistry','Physics','Maths','Biology']
print(f'subjects = {subjects}')
print()
subjects.remove("Maths")
print('output after removing :',subjects)
print('---')

# 10. The reverse() method reverses the sorting order of the elements.

numbers = [1,2,3,4,5,6]
print(f'numbers = {numbers}')
print()
numbers.reverse()
print('output after reverse: ',numbers)
print('---')

# 11. The sort() method sorts the list ascending by default.

colors = ['Red','Black','White','Pink']
print(f'colors = {colors}')
print()
colors.sort()
print('output after sort: ',colors)
print('---')
