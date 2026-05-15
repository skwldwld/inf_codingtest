input = 20

def find_prime_list_under_number(number):
    # 소수: 약수가 1과 자기자신뿐인 수
    # 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환
    # 1. 이중 for문
    #   숫자 하나하나마다 for문 돌려서 약수가 1과 자신뿐인지
    # 2. 앞의 수들을 포함하는 수인지?

    prime_numbers = [2]
    flag = False
    for i in range(number - 2):
        for j in prime_numbers:
            if (i + 2) % j == 0:
                flag = False
                break
            else:
                flag = True
        if flag is True:
            prime_numbers.append(i + 2)
            flag = False

    return prime_numbers


result = find_prime_list_under_number(input)
print(result)