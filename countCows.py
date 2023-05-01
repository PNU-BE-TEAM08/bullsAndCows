def countCows(number, answer):
    cows = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if(str(number[i]) == str(answer[j]) and i != j):
                cows += 1
    return cows
