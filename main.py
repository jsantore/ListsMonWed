
courses_to_take = ["comp151", "Comp143", "Math130", "Math120", "Math161"]
print(f"Starting list of classes {courses_to_take}")
courses_to_take.insert(2,"Comp152")
print(courses_to_take)
courses_to_take[2]="Cybf210"
print(courses_to_take)
my_course = input("What Upper level course will you take")
#courses_to_take.insert(6, my_course)
courses_to_take.append(my_course)
print(courses_to_take)
courses_to_take[7] = "Cybf350"
print(courses_to_take)