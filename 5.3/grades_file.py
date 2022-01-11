import random

name = input('Name (First & Last): ')

grades = []
for n in range(5):
    grades.append(random.randrange(101))

print('Here are your randomly-selected grades (hope you pass):')
for n in range(len(grades)):
    print(f'Grade {n+1}: {grades[n]}')

marks = open('WorkFolder/lists/marks.txt', "a")
marks.write(f"{(name)}\n")
marks.write(str(grades))

marks = open("WorkFolder/lists/marks.txt", "r")
print(marks.read())

marks.close()