def create_checklist():

# Keep inputting in assignments until you are done. When finished, input the word, "done".

  checklist = []
  while True:
    assignment = input("Enter an assignment (or 'done' to finish): ")
    if assignment == "done":
      break
    checklist.append(assignment)
  return checklist

checklist = create_checklist()
print("Here is your checklist:")
print(checklist)
