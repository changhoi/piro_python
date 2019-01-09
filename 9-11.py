voca = open('vocabulary.txt', 'w', encoding = 'utf-8')

while True:
    new_english = input("영어 단어를 입력하세요: ")
    if new_english == 'q':
        break
    voca.write(new_english + ": ")
    new_korean = input("한국어 뜻을 입력하세요: ")
    voca.write(new_korean + "\n")

voca.close()