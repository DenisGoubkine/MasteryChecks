import random
my_list = []

for i in range(1000):
    my_list.append(str(random.randrange(10, 100)))
print('  '.join(my_list))