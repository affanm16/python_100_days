#create a program of displaying qestions to the user like kbc
#use list data type to store the questions and correct answer
#display the final amount after winning

list=["welcome to KBC game"]
questions=["Current Railway Minister of India is","Which city is known as Pink City in India?","capital of india","How many states are there in India?","Where in India Gate located?"]
answers=["ashwini","jaipur","delhi","29","mumbai"]
prizes=[1000,2000,3000,4000,10000]


answers1 = input(questions[0])
if answers1.lower() == answers[0]:
    print("Correct answer. You have won",prizes[0])

    answer2 = input(questions[1])
    if answer2.lower() == answers[1]:
        print("Correct answer. You have won",prizes[1])

        answer3 = input(questions[2])
        if answer3.lower() == answers[2]:
            print("Correct answer. You have won", prizes[2])

            answer4 = input(questions[3])
            if answer4.lower() == answers[3]:
                print("Correct answer. You have won", prizes[3])

                answer5 =input(questions[4])
                if answer5.lower( )== answers[4]:
                    print("correct answer.You have won",prizes[4])
                else:
                    print("chal bsdk!!!🤣🤣🤣.your take home amount is",prizes[3])
            else:
                print("chal bsdk!!!🤣🤣🤣.Your take home amount is",prizes[2])
        else:
            print("chal bsdk!!!🤣🤣🤣.Your take home amount is",prizes[1])

    else:
        print("chal bsdk!!!🤣🤣🤣.Your take home amount is:",prizes[0])

else:
    print("chal bsdk!!!🤣🤣🤣" )

