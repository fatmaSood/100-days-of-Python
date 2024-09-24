# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height = 0
height_sum = 0

for heights in student_heights:
    height += 1

for total_sum in student_heights:
    height_sum += total_sum

average_heights = round(height_sum / height)
print(average_heights)
