import json
fruits = ('Apples', 'Oranges', 'Mangoes')

person = {
    'name': 'Amal',
    'age': 30
}

# print(person['name'])

for key in person:
    print(person[key])

# count = 0
# count+= 1
# f = ['alknx']
# f.clear()
# print(f)

users = [
    {
        'name':'John Doe',
        'email':'johndoe34@gmail.com'
    },
    {
        'name':'Jane Doe',
        'email':'janedoe30@gmail.com'
    }
]

print(users)
print(type(users))

usersjson = json.dumps(users)

print(usersjson)
print(type(usersjson))

usersback = json.loads(usersjson)

print(usersback)
print(type(usersback))

for user in users:
    name = user['name']
    print(f'Name: {name}')

