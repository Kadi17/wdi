import random
max_elements_dict = 15
max_elements_list = 10

disctionary = {}
#lsowanie długości słownika orazu kluczy i wartości
for i in range(0, random.randrange(2, max_elements_dict)):
    tab = []
    key = ''
    for i in range(0, random.randrange(2,max_elements_list)):
        tab.append(random.randrange(5))
        letter = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz'))
        key = key+letter
    
    disctionary[key]= tab
print('---------------------------------------------------------------------------------------')
print(disctionary)
print('---------------------------------------------------------------------------------------')
disctionary_2 = {}
#dodawanie warttości liczb w listach
for x in disctionary:
    sum = 0
    content = disctionary[x]
    key = x
    for i in content:
        sum = sum + i
    disctionary_2[key]= sum
print(disctionary_2)
print('---------------------------------------------------------------------------------------')
sorted_sum = sorted(disctionary_2.items(), key=lambda x:x[1], reverse=True)
converted_dict = dict(sorted_sum)
print(converted_dict)
print('---------------------------------------------------------------------------------------')

