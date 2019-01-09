from random import randint

chance = 4
ANSWER = randint(1, 20)
while chance != 0:
    res = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % chance))
    if ANSWER > res:
        chance -= 1
        if chance != 0:
            print("Up")
        else:
            break
    elif ANSWER < res:
        chance -= 1
        if chance != 0:
            print("Down")
        else:
            break
    else:
        break

if chance == 0:
    print("아쉽습니다. 정답은 %d였습니다." % ANSWER)
else:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - chance))


