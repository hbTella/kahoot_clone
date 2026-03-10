import random

print("welcome to our kahoots!")
# add score
# add a score variable to store our score 
score = 0
# take users input to get their name
name = input("What is your name?").strip()

print("Hello", name, "Lets start our game!")


# start with simple dummy questions to test

#answer = input("What language is this quiz written in?").strip().lower()

# we need to have a way to say "If you got it right then output correct, otherwise tell then wrong answer"
# = is for assigning a variable and == is to check if a value is equivalent to.

# if answer == "python":
#     print("Correct answer")
# # update score if answer is correct
#     score = score + 100
# else:
#     print("wrong answer")

# lets create a dictionary object with all our questions stored inside of it that we can access randomly

questions = {
    # Question1: answer1,
    "What language is this quiz written in?": {
        "options":["js", "python", "c++", "Ruby"],
        # from those options which one is correct?
        "answer":"python"
    },
    "what symbol is used to write a comment in python":{
        "options":["/", "~", "*", "#"],
        "answer": "#"
    },
    "What function is used to display text in our terminal":{
        "options":["Display", "touch", "print", "write"],
        "answer": "print"
    } 
}

# randomize the questions into a list
question_list = list(questions.keys())
#print(question_list) 
random.shuffle(question_list)

#print(questions[0])
# print(questions["What language is this quiz written in?"])
# print(questions.key())
print("Your Score is :", score)

#print(questions[1])
# come up with a way to loop over our questions
for question in question_list:
    print("\n" + question)
    # we need to define and then print all our options
    options = questions[question]["options"]
    for option in options:
        print(option)
    answer = input("Your answer:").strip().lower()
    if answer == questions[question]["answer"]:
        print("\n Correct! score = +100")
# update score if answer is correct
        score = score + 1
    else:
        print("wrong answer")
print("\n final score:", score)
# Lets see what our percentage correct was!
percentage = round((score/len(questions))* 100)
print("\n You got", percentage, "% correct!")

#print(question["What language is this quiz written in?"])


