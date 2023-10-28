users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}
unique = len(set(users))
dict['Уникальные посещения'] = unique
dict['Общее количество'] = len(users)

print(dict)