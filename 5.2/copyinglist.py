import random

my_list = []
list2 = []

for i in range(10):
    my_list.append(random.randint(1,100))


for i in range(len(my_list)):
    list2.append(my_list[i])


my_list[-1] = -7

for n in my_list:
    print(n, end= ' ')
print()
for m in list2:
    print(m, end= ' ')
print()
