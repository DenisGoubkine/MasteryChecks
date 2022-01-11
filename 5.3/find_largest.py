import random
my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 101))
for i in range(len(my_list)):
    print(my_list[i], end=' ')

maxnum = None
for num in my_list:
    if max(my_list):
        maxnum = max


print(f'\nThe largest number is {maxnum}')