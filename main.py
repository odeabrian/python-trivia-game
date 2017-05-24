score = 0
question = ["1. How many letters are in the alphabet?\na. 15 b. 26 c. 5 d. 11", "\n2. What do you mean line too long? a. b. c. d."]
answer = ["b", "a"]

# for i in question:
#
#     if input(question[0]) is answer[0]:
#         print("You're correct!")
#         score = score + 1
#     elif score is 0:
#         score = 0
#     else:
#         print("Sorry, better luck next time.")
#         score = score - 1
#     print("Score: " + str(score))

if input(question[0]) is answer[0]:
    print("You're correct!")
    score = score + 1
elif score is 0:
    score = 0
else:
    print("Sorry, better luck next time.")
    score = score - 1
print("Score: " + str(score))

if input(question[1]) is answer[1]:
    print("You're correct!")
    score = score + 1
# elif score is 0:
    score = 0
else:
    print("Sorry, better luck next time.")
    score = score - 1
print("Score: " + str(score))