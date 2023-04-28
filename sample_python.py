# # used to create new list using an existing list
# list_1=[2,3,4,5,1,-1,-3] # existing list
# new_list_1 = [x**2 for x in list_1] # creating new list with square of number
# print(list_1)
# new_list_1 = [x**2 if x>2 else x-100 for x in list_1] # creating new list with square of number where number is greater than 2
# print(new_list_1)
# car_list = ['ford', 'honda', 'toyota', 'suzuki'] # car brand list
# new_car_list = ['old_honda' if x =='honda' else  x for x in car_list] # change honda to old_honda and else keep same
# print(new_car_list)
# list_3 = [x for x in range(-3,5,1)] # creat a list with range 
# print(list_3)
# sample_sen = 'the rocket came bAck from mars' # a string 
# sample_sen_new = [x for x in sample_sen if x.lower() in 'aeiou'] # seperate vowels from string
# print(sample_sen_new)
# users = [
#     {'name':'jack', 'age': 20, 'country':'pak'},
#     {'name':'mark', 'age': 23, 'country':'ind'},
#     {'name':'zack', 'age': 29, 'country':'pak'}
# ] # list with dictionaries.
# new_name = [user['name'] for user in users if user['age'] > 20] # creating a list with names where age is greater than 20
# print(new_name)
# print('added from repo')
weight = [12,32,12,4]
height = [32,41,42,9]
import numpy as np
np_weight = np.array(height)
np_height = np.array(weight)
bmi = np_weight/(np_height *2)
print(bmi)