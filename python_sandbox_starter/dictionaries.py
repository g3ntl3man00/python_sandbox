# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Simple dictionary  
person= {
    'first_name':'John ',
    'last_name':'Doe',
    'age' : 19,
} 

# you can use the constructor too  

# if you wanna access an item you could do sum like dis 

# person.get('age')


# Add values 
# person['phone'] = '555-555-5555' 

# copy dictionaries
# person2 = person.copy()
# person2 ['city'] = 'LHr'

# remove an item 
# del(person['age'])

# Clear
# person.clear()
print(person)

# list of dictionaries/object (for js people )
people = [
    {'name': "John", 'age': 69},
    {'name': "Kelly", 'age': 45},
]

 
print(people[1]['name']) 
