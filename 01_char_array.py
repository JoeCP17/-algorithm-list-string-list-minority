# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
#
# 입,출력 예시와 같이 입력 문자열에 나타나는
# 각 알파벳의 종류,갯수를 요약하여 나타내시오.

# 문자의 개수를 셀 count 필요
# 들어있는 문자 파악 (sort 정렬 이용)
#
def summarize_string(input_str):
    count = 0
    same_array = ' '
    index = len(input_str)

    for i in range(index - 1):
        if input_str[i] == input_str[i + 1]:  # 앞과 뒤의 글자가 서로 같을경우
            count += 1  # 카운트 1증가
        else:  # 다를경우
            same_array += input_str[i] + str(count + 1) + '/'  # 같았을때의 경우를 same_array에 추가
            count = 0  # 다른경우니까 카운트는 증가시키지 않는다.

    same_array += input_str[index - 1] + str(count + 1)  # for문을통해 구한 모든 문자와 수를 same_array에 저장

    return same_array  # same_array 반환


input_str = "acccdeee"

print(summarize_string(input_str))
