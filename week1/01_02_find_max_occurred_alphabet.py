def find_max_occurred_alphabet(string):
    data = dict()
    for char in string:
        if char.isalpha():
            if char in data:
                data[char] += 1
            else:
                data[char] = 1

    return max(data, key=data.get)

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))