def grade_needed(current_grade, final_grade_weight, desired_grade):

  current_grade /= 100
  final_grade_weight /= 100
  desired_grade /= 100
  return (desired_grade - current_grade * (1 - final_grade_weight)) / final_grade_weight

current_grade = float(input("Enter your current grade as a percentage: "))
final_grade_weight = float(input("Enter the weight of the final exam as a percentage: "))
desired_grade = float(input("Enter your desired overall grade as a percentage: "))

grade_needed = grade_needed(current_grade, final_grade_weight, desired_grade)
print("")
print("Your current grade is: " + str(current_grade))
print("The final exam weight is: " + str(final_grade_weight))
print("Your desired grade is: " + str(desired_grade))
print("")
print(f"You need to get a grade of {grade_needed * 100}% on the final exam.")
print("")