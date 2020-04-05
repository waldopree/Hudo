# import randomgen function
import randomgen
import recq

throw = 0
stop = False

while throw < 3 and stop == False:
    throw += 1
    dices = randomgen.random_cal()
    print(dices)

    if throw < 3:
        again = input("Again (y) or stop (n): ")
        if again == "n":
            stop = True
            print("Good job, you got: " + str(dices))
