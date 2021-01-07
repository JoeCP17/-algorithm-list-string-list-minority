# 0과 1로만 이루어진 문자열이 주어졌을 때,
# 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 예를 들어 S=0001100 일 때,

# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0  # 1 -> 0으로 변환될때를 저장하기 위한 변수 선언
    count_to_all_one = 0  # 0 -> 1로 변환될때 저장하기 위한 변수 선언

    # 첫 글자가 0 인지 혹은 1인지 판단하기 위한 if문
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_one += 1

    for i in range(len(string) - 1):       # 첫글자를 제외한 길이 분석
        if string[i] != string[i + 1]:     # 다음 문자열 변수 i가 다음 숫자와 같지 않다면
            if string[i + 1] == '0':       # 중첩 if문을 통해 다음 글자가 0일 경우
                count_to_all_one += 1      # count_to_all_one 변수에 1을 추가
            if string[i + 1] == '1':       # 중첩 if문을 통해 다음 글자가 1일 경우
                count_to_all_zero += 1     # count_to_all_zero 변수에 1을 추가

    return min(count_to_all_one, count_to_all_zero)  # 파이썬 문법 min()을 쓰면 이 두개의 경우중 비교하여 가장 작은 수를 return 한다.


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
