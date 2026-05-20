input = "011110"
# input = "0001111000"
# input = "0101001010"
# input = "01010001101"


def cal_repeat(repeat, max_repeat, numlist):
    for i in numlist:
        # 최다반복 길이, 끝나는 위치 구하기
        if i > 0:
            if numlist[i - 1] == numlist[i]:
                repeat += 1
                if max_repeat < repeat:
                    max_repeat = repeat
            else:
                if max_repeat != repeat:
                    max_index = i - 1
                    repeat = 0

    return repeat, max_repeat

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 0의 수가 많은지, 1의 수가 많은지 구하기
    # 붙어 있는 수가 있는지
    # 적은 숫자의 개수만큼 뒤집
    # 만약 적은 숫자들이 여러개 붙어 있다면 -> 붙어 있는걸 하나로 치기

    # 한 자 한 자 배열에 넣기
    # 붙어있는 수 개수 세기

    # for문 - 반복되기 시작하는 인덱스, 몇 개 연속으로 반복되는지 저장. 가장 큰 것만 저장하면 됨
    # 붙어있는 게 가장 많은 곳의 바로 옆에 있는 수를 뒤집자 (한개가 될수도, 여러개가 될수도)
    # 옆에 있는 수가 몇개 연속으로 있는지 세기
    # for문 - 반복 끝나는 데부터 끝까지. 숫자가 바뀌기 전까지
    # 끝나는 인덱스 저장
    # 배열에서 가장큰반복 끝나는 인덱스 + 1 ~ 숫자 바뀌기 전 마지막 인덱스의 숫자 반전해주기 - 비트 연산자

    # 만약 숫자 다른게 하나라면 그때는 그 수만 뒤집기

    count_zero = string.count('0')
    count_one = string.count('1')
    numlist = [0] * len(string)

    max_index = 0   # 반복이 끝나는 지점
    max_repeat = 0  # 가장 많이 반복되는 길이
    repeat = 0      # 반복되는 길이

    repeat_count = 0

    for i in range(len(string)):
        numlist[i] = int(string[i])

    repeat, max_repeat = cal_repeat(repeat, max_repeat, numlist)

    # 반복이 없는 경우
    if max_repeat == 0:
        if count_zero >= count_one: return count_one
        else: return count_zero

    # 반복이 있는 경우
    else:
        repeat_count += 1
        part_index, part_max_repeat = cal_repeat(0, 1, numlist[max_index::])
        for i in numlist[max_index::]:
            if part_max_repeat > 1:
                numlist[max_index + i + 1] = ~numlist[max_index + i + 1]

        for i in numlist[:max_index:]:
            if part_max_repeat > 1:
                numlist[max_index + i + 1] = ~numlist[max_index + i + 1]

    return repeat_count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)