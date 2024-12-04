from queue import PriorityQueue

print("Lets Play a Quiz Game!\n")

playing = input("Would You Like to play a game? (Y/N): ").upper()
Questions = ["\nWhat come after A ?",
             "\nWho is the 25th president of the United States?",
             "\nWhat race is Neil Armstrong?"]

Answers = ["B", "William McKinley", "Black"]


def play(Questions, Answers, score=0):
    print("Alright, Here r some question! ")
    for i in range(len(Questions)):
        print(Questions[i])
        user_answer = input("Ans: ")

        if user_answer.strip().lower() == Answers[i].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! \n The Correct Answers is {Answers[i]}.")
    print(f"Your final score is {score} out of {len(Questions)}")


if playing == "Y":
    play(Questions, Answers)
else:
    print("Have a nice day!")
    quit()
