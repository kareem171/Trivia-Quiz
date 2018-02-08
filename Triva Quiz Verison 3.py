'''

'''

print("This is a quiz that tests your knowledge on Greek mythology")

'''
'''

name= input("Enter your name: ")
print("Hi there,", name, ",", "Are you ready to start the quiz?")


print( " I will ask you 6 questions and give you three choices")
print("Select which choice is the correct answer, A, B, or C")
print("---------------------------")


#Set the score of the quiz to 0
score=0
score= int(score)

while True: 
    #question 1
    print("Question 1: Who is the god of the sea?")
    print("")
    print("A: Poseidon")
    print("B: Hades")
    print("C: Athena")
    print("")

    Q1answer = "A" #correct answer
    Q1response = input("Your answer: ")

    if Q1response == "A" or Q1response == "a":
        print("Correct answer:", Q1answer)
        score = score+1
    elif Q1response != "A" or Q1response != "a":
        print("Sorry, incorrect.")

    print("Your current score is", score, "out of 6.")

    #question 2
    print("Question 2: Ares was the god what?")
    print("")
    print("A: love")
    print("B: war")
    print("C: thunder")
    print("")

    Q2answer = "B" #correct answer
    Q2response = input("Your answer: ")

    if Q2response == "B" or Q2response == "b":
        print("Correct answer:", Q2answer)
        score = score+1
    elif Q2response != "B" or Q2response != "b":
        print("Sorry, incorrect.")

    print("Your current score is", score, "out of 6.")

    #question 3
    print("Question 3: What is a demigod?")
    print("")
    print("A: child of a god and human")
    print("B: a lesser powerful god?")
    print("C: children of Demeter?")
    print("")

    Q3answer = "A" #correct answer
    Q3response = input("Your answer: ")

    if Q3response == "A" or Q3response == "a":
        print("Correct answer:", Q3answer)
        score = score+1
    elif Q3response != "A" or Q3response != "a":
        print("Sorry, incorrect.")

    print("Your current score is", score, "out of 6.")

    #question 4
    print("Question 4: How was Aphrodite created?")
    print("")
    print("A: she was concieved by Hera")
    print("B: she was a piece of Zues")
    print("C: she appeared of out foam from the sea")
    print("")

    Q4answer = "C" #correct answer
    Q4response = input("Your answer: ")

    if Q4response == "C" or Q4response == "c":
        print("Correct answer:", Q4answer)
        score = score+1
    elif Q4response != "C" or Q4response != "c":
        print("Sorry, incorrect.")

    print("Your current score is", score, "out of 6.")

    #question 5
    print("Question 5: Who are the parents of gods?")
    print("")
    print("A: Gaea and Uranus")
    print("B: They have no parents")
    print("C: Titans")
    print("")

    Q5answer = "C" #correct answer
    Q5response = input("Your answer: ")

    if Q5response == "C" or Q5response == "c":
        print("Correct answer :", Q5answer)
        score = score+1
    elif Q5response != "C" or Q5response != "c":
        print("Sorry, incorrect.")

    print("Your current score is", score, "out of 6.")

    #question 6
    print("Question 6: Which giant is the anti-Zues?")
    KAprint("")
    print("A: Enceladus")
    print("B: Porphyrion")
    print("C: Polybotes")
    print("")

    Q6answer = "B" #correct answer
    Q6response = input("Your answer: ")

    if Q6response == "B" or Q6response == "b":
        print("Correct answer:", Q6answer)
        score = score+1
    elif Q6response != "B" or Q6response != "b":
        print("Sorry, incorrect.")

    final_score = (score*100)/6
    print("You ended with the score of" , str(final_score), "percent")
    print("Congrats! your score is", score, "out of 6.")

    answer= input("Would you like to take the quiz again?")

    if answer == "Yes" or answer == "yes":
        continue
    else:
        break




    
