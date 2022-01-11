import random
my_list = []

for n in range(10):
    my_list.append(random.randrange(1, 51))
for i in range(len(my_list)):
    print(my_list[i], end= ' ')
print()

num = int(input("Please Provide An Integer: "))
count = 0
found = False

for m in range(len(my_list)):
    if num == (my_list[m]):
        found = True
        count +=1
    else: 
        continue
print()
if found:
    print(f'{num} was found {count} times.')
else:
    print('Number not found')
