l1 = [1, 2, 3]
l2 = ['manoj', 'kumar', 'lodhi', 'ok']
result = zip(l1, l2)
print(type(result))
# print(set(result)) # {(1, 'manoj'), (3, 'lodhi'), (2, 'kumar')}
print(dict(result)) # {1: 'manoj', 2: 'kumar', 3: 'lodhi'}
