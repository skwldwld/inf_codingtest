input = "abadabac"

def find_not_repeating_first_character(string):
    arr = [0] * 26

    for i in string:
        arr_index = ord(i) - ord('a')
        arr[arr_index] += 1

    for j in string:
        arr_index = ord(j) - ord('a')
        if arr[arr_index] == 1:
            return j

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))