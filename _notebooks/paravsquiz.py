import getpass, sys

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)
    
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 6
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
rsp = question_with_response("Are you ready to take a test?")
if rsp == "yes":
    print("Great, here is your first question!")
else:
    print("Okay, come back when you're ready...")

rsp = question_with_response("What command is used to include other functions that are developed?")
if rsp == "import":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What command in this example is used to evaluate a response?")
if rsp == "if":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("Grouping a sequence of commands is called _____ _____.")
if rsp == "procedural abstraction":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What is the command for a string concatenation?")
if rsp == "+":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What can be found below the code cell in Jupyter notebook?")
if rsp == "output":
    print(rsp + "is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
print()
