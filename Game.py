
import random
import datetime

Players = int(input("Enter The Number Of Players { 1 , 2 } : "))
FirstName = None
SecondName = None
NextLevel = "y"
Level =1

print("")

class MyGame:
    def __init__(self):
        pass

    def FirstNumber(self):
        return random.randrange(0,13)

    def TheOperator1(self):
        ope = "+"
        return ope

    def TheOperator2(self):
        Operators = ["+" , "-" ]
        ope = random.choice(Operators)
        return ope

    def TheOperator3(self):
        Operators = ["+" , "-" , "*"]
        ope = random.choice(Operators)
        return ope

    def TheOperator4(self):
        Operators = ["+" , "-" , "/" , "*"]
        ope = random.choice(Operators)
        return ope


    def SecondNumber(self):
        return (random.randrange(0,13))

    def Answer(self):
        answer = int(input("= ").strip())
        return answer


if Players == 1:
    FirstName = input("Enter The User Name : ").title()

if Players == 2:
    FirstName = input("Entre First USerName : ").title()
    SecondName = input("Entre Second USerName : ").title()



while NextLevel == "y":

    FinalTimeOne = 0
    FinalTimeTwo = 0
    FirstTries = 12
    FirstGrade = 0
    SecondTries = 12
    SecondGrade = 0

    while(FirstTries >0 and SecondTries >0):
        StartOne = datetime.datetime.now()
        game = MyGame()
        fnum=game.FirstNumber()

        if Level ==1:
            ope = game.TheOperator1()

        elif Level ==2:
            ope = game.TheOperator2()

        elif Level == 2:
            ope = game.TheOperator2()

        else:
            ope = game.TheOperator2()

        snum = game.SecondNumber()

        if ope=="/" and snum ==0:
            continue

        print(f"{FirstName} Turn")
        print(fnum , end=" ")
        print(ope , end=" ")
        print(snum , end = " ")


        if ope == "+":
            Result = fnum + snum

        elif ope == "-":
            Result = fnum-snum

        elif ope == "/":
            Result = int(fnum / snum)

        else:
            Result = fnum * snum

        finalanswer = game.Answer()


        line = 3
        points = 0
        space = 0
        if finalanswer == Result:

            FirstGrade += 2
            space =0
            while space < line:
                print(" " , end=" ")
                space +=1
                if space < line:
                    continue
                while points < FirstGrade:
                    print("*" , end = " ")
                    points += 2
                    if points == 2 or points ==8:
                        print(" ")
                        break
                line -= 1
                space = 0
                continue
            if FirstGrade == 18:
                print("")
                break


        else:
            line = 3
            print(f"{FirstName} Your Answer Is Wrong, The Correct Answer Is : {Result}")
            space = 0
            while space < line:
                print(" ", end=" ")
                space += 1
                if space < line:
                    continue
                while points < FirstGrade-2:
                    print("*", end=" ")
                    points += 2

                    if points == 2 or points == 8:
                        print(" ")
                        break

                line -= 1
                space = 0
                continue
            if FirstGrade == 0:
                FirstGrade = FirstGrade
            else:
                FirstGrade -= 2

        FirstTries -= 1

        print(" ")

        EndOne = datetime.datetime.now() # Player One End Time
        PlayerTimeOne = EndOne - StartOne
        FinalTimeOne +=  PlayerTimeOne.total_seconds()
        if Players ==2 :

            while (SecondTries > 0):
                StartTwo = datetime.datetime.now()   # The Began Of The Player Two Time

                game = MyGame()
                fnum = game.FirstNumber()

                if Level == 1:
                    ope = game.TheOperator1()

                elif Level == 2:
                    ope = game.TheOperator2()

                elif Level == 2:
                    ope = game.TheOperator2()

                else:
                    ope = game.TheOperator2()

                snum = game.SecondNumber()

                if ope == "/" and snum == 0:
                    continue

                print(f"{SecondName} Turn")
                print(fnum, end=" ")
                print(ope, end=" ")
                print(snum, end=" ")

                if ope == "+":
                    Result = fnum + snum

                elif ope == "-":
                    Result = fnum - snum

                elif ope == "/":
                    Result = int(fnum / snum)

                else:
                    Result = fnum * snum

                finalanswer = game.Answer()

                line = 3
                points = 0
                space = 0
                if finalanswer == Result:

                    SecondGrade += 2
                    space = 0
                    while space < line:
                        print(" ", end=" ")
                        space += 1
                        if space < line:
                            continue
                        while points < SecondGrade:
                            print("*", end=" ")
                            points += 2
                            if points == 2 or points == 8:
                                print(" ")
                                break
                        line -= 1
                        space = 0
                        continue
                    if SecondGrade == 18:
                        print("")
                        break


                else:
                    line = 3
                    print(f"{SecondName} Your Answer Is Wrong, The Correct Answer Is : {Result}")
                    space = 0
                    while space < line:
                        print(" ", end=" ")
                        space += 1
                        if space < line:
                            continue
                        while points < SecondGrade - 2:
                            print("*", end=" ")
                            points += 2

                            if points == 2 or points == 8:
                                print(" ")
                                break

                        line -= 1
                        space = 0
                        continue
                    if SecondGrade ==0 :
                         SecondGrade = SecondGrade
                    else:
                        SecondGrade -= 2

                EndTwo = datetime.datetime.now()
                PlayerTimeTwo = EndTwo - StartTwo
                FinalTimeTwo += PlayerTimeTwo.total_seconds()
                SecondTries -= 1

                print(" ")
                break

            if  SecondGrade == 18:
                break

    if FirstGrade == 18:

        if FinalTimeOne < 30:
            print(f"Congratulation {FirstName} You Win, You Done In Time {FinalTimeOne}")

        else:
            print(f"{FirstName} Your Time Is End Before You Done, You Done In Time {FinalTimeOne} Be Faster In Next Time")

        if Level == 4:
            print(f"Congratulation {FirstName} You Finish All Levels")
            break

        NextLevel = input("Enter {y} To Continue Next Level or {n} To Quit : ").strip().lower()
        if NextLevel == "y":
            Level += 1
            continue


    elif SecondGrade == 18:
        if FinalTimeTwo < 30:
            print(f"Congratulation {SecondName} You Win, You Done In Time {FinalTimeTwo}")

            if Level == 4:
                print(f"Congratulation {SecondName} You Finish All Levels")
                break

            NextLevel = input("Enter {y} To Continue Next Level or {n} To Quit : ").strip().lower()
            if NextLevel == "y":
                Level += 1
                continue

        else:
            print(
                f"{SecondName} Your Time Is End Before You Done, You Done In Time {FinalTimeTwo} Be Faster In Next Time")

    else :
        print("There Is No Winner, Good Luck Next Time")
        break






