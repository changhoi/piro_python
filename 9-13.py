voca = open('vocabulary.txt', 'r', encoding = 'utf-8')

for word in voca:
    temp = word.split(': ')
    i = 0
    for original in temp:
        temp[i] = original.strip()
        i += 1

    korean = temp[1]
    english = temp[0]
    user_answer = input(korean + ": ")
    if user_answer == english:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 " + english + "입니다.\n")

voca.close()