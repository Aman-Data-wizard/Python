
attendance_records = [
    {101, 102, 103, 104},  # Day 1
    {102, 103, 105, 106},  # Day 2
    {101, 103, 104, 107}   # Day 3
]
attendance_count = {}

for day in attendance_records:
    for student_id in day:
        if student_id in attendance_count:
            attendance_count[student_id] += 1
        else:
            attendance_count[student_id] = 1

max_attendance = 0
for count in attendance_count.values():
    if count > max_attendance:
        max_attendance = count

most_frequent_attendees = set()
less_than_two_classes = set()
for student, count in attendance_count.items():
    if count == max_attendance:
        most_frequent_attendees.add(student)
    if count < 2:
        less_than_two_classes.add(student)

print("Most frequent attendees:", most_frequent_attendees)
print("Students with less than 2 classes:", less_than_two_classes)
