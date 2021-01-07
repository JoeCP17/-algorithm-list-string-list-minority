# 소수 나열하기 [숙제]

# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 1 , 3 , 5 , 7 ,11 , 13 ,17,19
input = 20


def find_prime_list_under_number(number):
    #under_number = []
    #for num in range(2, number + 1):      # num 범위 : 2 ~number+1

           # num이 20이라 가정했을 경우
           #i를 2~19까지
           # 이렇게 계산할시 중복되어 계산되는 경우도 많다.

        #for i in range(2, num):           # i 범위 :  2 ~num-1
            #if num % i == 0:
               #break
       # else:
           # under_number.append(num)

   # return under_number


   #under_number = []
   # for num in range(2, number + 1):  # num 범위 : 2 ~number+1

       # for i in under_number:  # 중복되지 않고 소수만을 찾아 검사할수 있다.

            #if num % i == 0:
               # break
       # else:
            #under_number.append(num)

   # return under_number


# 소수는 자기 자신과 1외 에는 아무것도 나눌수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데 , 몫과 나누는 수 둘중 하나는
# 반드시 N의 제곱근 이하

    under_number = []
    for num in range(2, number + 1):  # num 범위 : 2 ~number+1

        for i in under_number:  # 중복되지 않고 소수만을 찾아 검사할수 있다.

                 #소수일때 제곱근 까지만 나누어줄수 있다.
            if num % i == 0 and i * i <= num: # 전체를 계산하는것이 아닌 2,3 정도 까지만 계산함으로 성능이 훨씬 개선됨
                # i 를 2, 3만 비교 (전체 input= 20 이므로 루트20 으로나눌시 2,3)
                break
        else:
            under_number.append(num)

    return under_number


result = find_prime_list_under_number(input)
print(result)