import random
my_list = []

for n in range(10):
    my_list.append(random.randrange(1, 51))
for i in range(len(my_list)):
    print(my_list[i], end= ' ')
print()

num = int(input("Please Provide An Integer: "))
found = False
x = 0

for m in range(len(my_list)):
    if num == (my_list[m]):
        print(f'{num} is at index {m}')
    else: 
        continue
print()

if found:
    print(f"{num} is not in the list")

