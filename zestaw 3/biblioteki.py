import random
max_items = 15
max_elements_list = 10

test = {'abc':[1,2,3,4,5], 'cdf':[1,4,54]}
#print(test['abc'])
disctionary = {}
for i in range(0, random.randrange(2, max_items)):
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

