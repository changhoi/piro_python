from random import randint

voca = open('vocabulary.txt', 'r', encoding='utf-8')
adv_voca = {}
number = 0
for i in voca:
    number += 1
    word_set = i.split(': ')
    word_set[1] = word_set[1].strip()
    adv_voca[number] = word_set

while True:
    next = randint(1, len(list(adv_voca.keys())))
    test_word = adv_voca[next]
    answer = input(test_word[1] + ": ")
    if answer == 'q':
        break

    if answer == test_word[0]:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 temple입니다.")

voca.close()