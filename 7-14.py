from random import randint

ANSWER = []
i = 0

while i < 3:
    val = randint(0, 9)
    if val not in ANSWER:
        ANSWER.append(val)
        i += 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")

count = 0
#맞출 때까지 게임 돌리기
while True:
    count += 1
    userInput = []
    #세 개의 숫자 받기
    while True:
        temp = int(input("1번째 수를 입력하세요: "))
        if temp in userInput:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif temp < 0 or temp > 9:
            print("범위를 벗어나는 수 입니다. 다시 입력해주세요.")
            continue
        else:
            userInput.append(temp);
            break
        break

    while True:
        temp = int(input("2번째 수를 입력하세요: "))
        if temp in userInput:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif temp < 0 or temp > 9:
            print("범위를 벗어나는 수 입니다. 다시 입력해주세요.")
            continue
        else:
            userInput.append(temp);
            break
        break

    while True:
        temp = int(input("3번째 수를 입력하세요: "))
        if temp in userInput:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif temp < 0 or temp > 9:
            print("범위를 벗어나는 수 입니다. 다시 입력해주세요.")
            continue
        else:
            userInput.append(temp);
            break
        break

    #스트라이크, 볼 세기
    strike = 0
    ball = 0
    i = 0
    while i < 3:
        if userInput[i] == ANSWER[i]:
            strike += 1
            i += 1
        elif userInput[i] in ANSWER:
            ball += 1
            i += 1
        else:
            i += 1

    #3스트라이크면 게임 종료 아니면 다시 돌기
    if strike == 3:
        print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)
        break
    else:
        print("%dS %dB" % (strike, ball))



