
students_names = open("names.txt", "r")

# print(students_names.readable())
# print(students_names.readlines(2))
# print(students_names.read())

for names in students_names.readlines():
    print(names)

students_names.close()