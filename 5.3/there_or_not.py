import random

my_list = []

for i in range(10):
    my_list.append(random.randrange(1, 51))
    
for m in range(len(my_list)):
    print(my_list[m], end = ' ')

integer = int(input("\nValue to find: "))

found = False
foundamount = 0
for n in range(len(my_list)):
    if integer == my_list[n]:
        found = True
        foundamount += 1
    else:
        continue

if found:
    print(f'The number was found {foundamount} time within the list')
elif not found:
    print('Not found once')