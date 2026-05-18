input = "011110"
# input = "0001111000"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 0의 수가 많은지, 1의 수가 많은지 구하기
    # 붙어 있는 수가 있는지
    # 적은 숫자의 개수만큼 뒤집
    # 만약 적은 숫자들이 여러개 붙어 있다면 -> 붙어 있는걸 하나로 치기

    # 붙어있는 수 개수 세기
    # 붙어있는 수끼리 비교. 어떤게 더 적은지
    # 많은 걸 뒤집기
    # ㅎㅡㅁ냥이 이거 언제 아 푸니
    count_zero = string.count('0')
    count_one = string.count('1')

    if (count_zero == count_one):
        

    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)