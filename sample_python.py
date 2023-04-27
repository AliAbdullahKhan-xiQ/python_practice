# used to create new list using an existing list
list_1=[2,3,4,5,1,-1,-3]
new_list_1 = [x**2 for x in list_1]
print(list_1)
new_list_1 = [x**2 if x>2 else x-100 for x in list_1]
print(new_list_1)
car_list = ['ford', 'honda', 'toyota', 'suzuki']
new_car_list = ['old_honda' if x =='honda' else  x for x in car_list]
print(new_car_list)
list_3 = [x for x in range(-3,5,1)]
print(list_3)
sample_sen = 'the rocket came bAck from mars'
sample_sen_new = [x for x in sample_sen if x.lower() in 'aeiou']
print(sample_sen_new)
users = [
    {'name':'jack', 'age': 20, 'country':'pak'},
    {'name':'mark', 'age': 23, 'country':'ind'},
    {'name':'zack', 'age': 29, 'country':'pak'}
]
new_name = [{'name': user['name'],'age': user['age']} for user in users if user['age'] > 20]
print(new_name)