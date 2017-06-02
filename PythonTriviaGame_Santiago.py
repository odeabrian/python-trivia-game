print ("Welcome to Python Trivia!")

score = 0

question = ["1. How many times has the United States been at war with Great Britain? \n a. One b. Two c. Three d. Four\n", "2. Which state was the last to be annexed into the United States? \n a. Alaska b. Hawaii c. Puerto Rico d. Oregon\n", "3. What is the most popular breed of dog in the United States? \n a. Labrador Retriever b. Poodle c. Chihuahua d. Pug\n", "4. What was the original flavor of filling in Twinkies? \n a. Coconut b. Vanilla c. Chocolate d. Banana Cream\n", "5. How many species of felines are there in the world? \n a. 28 b. 56 c. 36 d. 109\n", "6. What is the national animal of Scotland? \n a. Dragon b. Beagle c. Unicorn d. Sheep\n", "7. How many Disney Princesses are there? \n a. 10 b. 11 c. 12 d. 13\n", "8. Who was the last man to walk on the moon? \n a. Captain Eugene Cernan b. Neil Armstrong c. Buzz Lightyear d. Savva Petrikov\n", "9. How many planets are in our solar system? \n a. 8 b. 9 c. 10 d. 11 \n", "10. Which of the five senses does a dolphin lack? \n a. Sight b. Taste c. Hearing c. d. Smell\n"]

answer = ["b", "b", "a", "d", "c", "c", "b", "a", "a", "d"]

# Question 1
if input(question[0]) == answer[0]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))
print("Explanation: America has gone to war with Great Britain during the Revolutionary War and the war of 1812\n")

# Question 2
if input(question[1]) == answer[1]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))
print("Hawaii earned its statehood in the year of 1898")

# Question 3
if input(question[2]) == answer[2]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))

# Question 4
if input(question[3]) == answer[3]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))

# Question 5
if input(question[4]) == answer[4]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print ("Score = " + str(score))

# Question 6
if input(question[5]) == answer[5]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print ("Score = " + str(score))

# Question 7
if input(question[6]) == answer[6]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))
print("Explanation: The following Disney Princesses include Snow white, Cinderella, Aurora, Ariel, Belle, Jasmine, Pocahontas, Mulan, Tiana, Rapunzel, and Merida/n")

# Question 8
if input(question[7]) == answer[7]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))

# Question 9
if input(question[8]) == answer[8]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))
print("Explanation: Pluto is a dwarf planet, so it doesnt count!\n")

# Question 10
if input(question[9]) == answer[9]:
    score = score + 1
elif score == 0:
    score = 0
else:
    score = score - 1
print("Score = " + str(score))

# written_question = input ("1. What does the U.S.S.R stand for? \n")
#
# written_answer = ["Union of Soviet Socialist Republic \n"]
#
# # Question 11 (Bonus)
# if input (written_question) = str(written_answer[1])
#     score = score + 5

