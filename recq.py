import randomgen

def recog(list):
    ones = list.count(1)
    twos = list.count(2)
    threes = list.count(3)
    fours = list.count(4)
    fives = list.count(5)
    six = list.count(6)

    list_amount = [ones, twos, threes, fours, fives, six]

    if ones == 5 or twos == 5 or threes == 5 or fours == 5 or fives == 5 or six == 5:
        yahtzee = "yahtzee"
        return yahtzee
    elif ones == 4 or twos == 4 or threes == 4 or fours == 4 or fives == 4 or six == 4:
        fourkind = "four of a kind"
        return fourkind
    elif 2 in list_amount:
        if 3 in list_amount:
            fullhouse = "fullhouse"
            return fullhouse
    elif ones == 3 or twos == 3 or threes == 3 or fours == 3 or fives == 3 or six == 3:
        threekind = "three of a kind"
        return threekind


# dices = randomgen.random_cal()
test_list = [2,2,1,3,4]
print(test_list)
result = recog(test_list)
print(result)
