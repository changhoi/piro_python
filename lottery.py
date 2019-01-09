#lottery.py

from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    list = []
    select = 0
    while select < 6:
        num = randint(1, 45)
        if num not in list:
            list.append(num)
            select += 1
    list.sort()
    return list

    # 코드를 입력하세요

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    list = generate_numbers()
    while True:
        bonus = randint(1,45)
        if bonus not in list:
            list.append(bonus)
            break
    return list
    # 코드를 입력하세요

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    for i in list1:
        if i in list2:
            count += 1
    return count
    # 코드를 입력하세요

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    correct = 0
    isBonusCorrect = False
    for i in numbers:
        if i in winning_numbers[0:6]:
            correct += 1

    if winning_numbers[6] in numbers:
        isBonusCorrect = True

    if correct == 6:
        return 1000000000
    elif correct == 5:
        if isBonusCorrect:
            return 50000000
        else:
            1000000
    elif correct == 4:
        return 50000
    elif correct == 3:
        return 5000
    else:
        return 0

    # 코드를 입력하세요