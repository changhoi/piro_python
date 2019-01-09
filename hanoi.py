def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg, end_peg, mid):
    if num_discs == 1:
        move_disk(num_discs, start_peg, end_peg)
    else:
        hanoi(num_discs - 1, start_peg, mid, end_peg)
        move_disk(num_discs, start_peg, end_peg)
        hanoi(num_discs - 1, mid, end_peg, start_peg)
    # 코드를 입력하세요.

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3, 2)