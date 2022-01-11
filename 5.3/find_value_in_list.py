import random

my_list = []

for i in range(10):
    my_list.append(random.randrange(1, 51))
    
for n in range(len(my_list)):
    print(my_list[n], end = ' ' )
print()
    
num = int(input('Please Proivde a Value: '))
print(f'Value to find: {num}\n')

for m in range(len(my_list)):
    if num == my_list[m]:
        print(f'{num} found in list')
    else:
        continue

    

# if num in my_list:
#     print(f'{num} is in the list')
# else:
#     print('Not in list')