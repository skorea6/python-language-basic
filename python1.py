#type : <class 'str'>
#print(type("안녕하세요"))

#큰따옴표 : /" | 작은 따옴표: /'
#print("안녕\"하세\'요")

#print("안녕" * 3)

#녕하
#print("안녕"[-1]+"하세요"[0])

# 마지막 숫자는 포함하지 않음!! 중요!! (녕하)
#print("안녕하세요"[1:3])

# 마지막 숫자는 포함하지 않음!! 중요!! (안녕)
#print("안녕하세요"[:2])

#len : 문자열 길이
#print(len("안녕"))

#print("5 + 7 = ", 5+7)
# 3 / 2 = 1.5
#print("3 / 2 = ", 3/2)
# 3 //2 = 1 (소수점 아래 때어버리기! 중요)
#print("3 // 2 = ", 3//2)
# 2의 몇승 (2의 3승)
#print("2**3 = ", 2**3)

#a1 = 30
#a1 += 10
#a1 += 50
#print(a1)

#a2 = input("인사말을 입력하세요")
#print(a2)


# <int(), float(), str()>
#s1 = input("s1: ")
#int_s1 = int(s1)

#s2 = input("s2")
#int_s2 = int(s2)

#print("문자열 더하기 : ", s1+s2) #2030
#print("숫자 더하기 : ", int_s1+int_s2) #50

#s3 = "{}".format(10)
#s4 = "{:5d}".format(10) #5칸 앞에서 밀기

#빈칸을 0으로 채우기
#s5 = "{:05d}".format(10) #5칸 앞에서 밀기

#기호와 함께 출력
#s6 = "{:+d}".format(-52) #-52
#s7 = "{:=+5d}".format(-52) # 기호를 앞으로 밀기, -    52

#의미없는 소수점 제거
#s8 = 52.0
#s9 = "{:g}".format(s8)

#대소문자 바꾸기
#a = "Hello Everyone"
#print(a.upper())
#print(a.lower())

#문자열 양옆 공백 제거 (왼쪽: lstrip, 오른쪽: rstrip)
#a1 = "       안  녕   "
#print(a1.strip())

"""
isalnum() : 알파벳 또는 숫자로만 구성됨?
isalpha() : 알파벳으로만 구성됨?
isidentifier(): 식별자로 사용 가능?
isdecimal() : 정수 형태?
isdigit() : 숫자 맞음?
isspace() : 공백으로만 구성됨?
islower() : 소문자로만 구성됨?
isupper() : 대문자로만 구성됨?
"""
#print("TrainA10".isalnum())

#find 함수 (왼쪽부터 찾음)
#output_a = "안녕안녕하세요".find("안녕")
#print(output_a) #0 (0번째 자리에 있는것, 0)

#rfind 함수 (오른쪽부터 찾음)
#output_a = "안녕안녕하세요".rfind("안녕")
#print(output_a) #2 (2번째 자리에 있는것, 0 1 2)

#in 연산자
#print("안녕" in "안녕하세요")

#split 함수
#a2 = "10 20 30 40 50".split(" ")
#print(a2) #['10', '20', '30', '40', '50']

#not 연산자
#x=10
#under_20 = x<20
#print("not under_20", not under_20)

#IF
#number = 20
#if number > 0:
#    print("양수")

#날짜/시간 + elif (else if)
#import datetime
#now = datetime.datetime.now()
#if 9 <= now.month <= 11:
#    print("이번달은 {}월로 가을입니다!".format(now.month))
#elif 3 <= now.month <= 5:
 #   print("이번달은 {}월로 봄입니다!".format(now.month))

#리스트
#list_a = [273,"하이","hi",True,39]
#print(list_a[-3][0]) #h
#list_b = [[1, 2, 3], [1, 2, 3], [6, 2, 3]]
#print(list_b[2][0])

#리스트에 요소 추가 append,insert,extend
#list_c = [1,2,3]
#list_c.append(4)
#list_c.insert(2,10) #2번째에 10을 추가
#list_c.extend([8,9,10]) #한번에 여러 요소 추가
#print(list_c)

#리스트 인덱스로 제거
#list_e = [1, 2, 3, 4]
#del list_d[1] #del list_d[:3] : 0,1,2 삭제
#pop(1)

#리스트 값으로 제거
#list_e = [1, 2, 1, 2]
#list_e.remove(2) #1, 1, 2 (앞쪽 1개만 제거됨)

#리스트 모두 제거
#list_e.clear()

#리스트 in/not in
#1 in list_e #true

#딕셔너리
#test1 = {
#    "name": "건조 망고",
#    "type": "당절임",
#    "ingredient": ["망고", "설탕", "소금"],
#    "origin": "필리핀"
#}
#test1["name"] = "건조 키위"
#test1["new"] = "새로운것 추가 가능"
#del test1["type"]
#print(test1["ingredient"][1])

# 딕셔너리 내부에 키가 있는가?
#key = input("키 입력: ")
#if key in test1:
#    print(test1[key])
#else:
#    print("no")

#value = test1.get(key)
#if value == None:
#    print("no")

#for문 출력
#for key in test1:
#    print(key, ": ", test1[key])

# Range
#n = 10
#print(list(range(0, 5)))
#print(list(range(0, 5, 2)))
#print(list(range(0, n // 2)))

# Range, Array, For
#array = [1, 2, 3, 4, 5]
#for i in range(len(array)):
#    print("{}번째 반복 : {}".format(i, array[i]))

# 역 For문
#for i in range(4, -1, -1):
#    print(i)

#for i in reversed(range(5)):
#    print(i)

#While
#list_test = [1, 2, 1, 2]
#value = 2
#while value in list_test:
#    list_test.remove(2)
#print(list_test)

#continue
#for number in numbers:
    #number가 10보다 작으면 다음 반복으로 넘어가기
#    if number < 10
#        continue
#    print(number)

#최대, 최소, 합계
#numbers = [103, 42, 273, 44, 46]
#print(max(numbers), min(numbers), sum(numbers))

#enumerate 함수 (배열에서 사용)
#example_list = ["A", "B", "C"]
#for i, value in enumerate(example_list):
#    print("{}번째 요소는 {}입니다".format(i,value))

#items 함수 (딕셔너리에서 사용)
#example = {
#    "키A": "값A",
#    "키B": "값B",
#    "키C": "값C"
#}

#print("items(): ", example.items())
#for key, element in example.items():
#   print("example[{}] = {}".format(key, element))

#리스트 내포
#array = [i*i for i in range(0, 20, 2) if i != 2]
#print(array)

#join 함수
#print("::".join(["1", "2", "3", "4", "5"]))

#이터레이터
#numbers = [1, 2, 3, 4, 5, 6]
#r_num = reversed(numbers)
#print(list(r_num))

#print(next(r_num))
#print(next(r_num))
#print(next(r_num))
#print(next(r_num))
#print(next(r_num))

#가변 매개변수
#def print_n_times(n, *values):
#    for i in range(n):
#        for value in values:
#            print(value)
#        print()
#print_n_times(3, "ㅎㅇ", "123", "와우")

#키워드 매개변수
#def print_n_times(*values, n=2):
#    for i in range(n):
#        for value in values:
#            print(value)
#        print()

#print_n_times("ㅎㅇ", "123", "와우", n=3)

#리턴 함수
#def return_test():
#    return 100
#print(return_test())

#범위 내부의 정수를 모두 더하는 함수
#def sum_all(start=0, end=100, step=1):
#    output = 0
#    for i in range(start, end + 1, step):
#        output += i
#    return output
#print(sum_all(end=10))

#재귀함수를 통한 팩토리얼
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)
#print(factorial(3))

#재귀함수를 통한 피보나치 수열
#counter = 0
#def fibonacci(n):
#    print("{}".format(n))
#    global counter
#    counter += 1
#    if n == 1:
#        return 1
#    if n == 2:
#        return 1
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(10))
#print(counter) #109번이나 반복하기 때문에 효율성 낮음

#메모화를 통한 피보나치 수열
#diction = {
#    1: 1,
#    2: 2
#}
#def fibonacci(n):
#    if n in diction:
#        return diction[n]
#    else:
#        output = fibonacci(n-1) + fibonacci(n-2)
#        diction[n] = output
#        return output

#패밀리 레스토랑 문제 (** 모르겠음 **)
#sitmax = 10
#memo = {}

#def family(people, sitmin):
#    key = str([people, sitmin])
#    if key in memo:
#        return memo[key]
#    if people < 0:
#        return 0
#    if people == 0:
#        return 1
#    count = 0
#    # 2 ~ 10 | 6-2, 2 |
#    for i in range(sitmin, sitmax + 1):
#        count += family(people - i, i)
#    memo[key] = count
#    return count

#print(family(6, 2))

# 튜플 -> 리스트와 비슷한데, 값 수정 불가
#a, b, c = (10, 20, 30)
#a, b, c = 10, 20, 30 # 괄호 없어도 됨
#print("a: ", a)

#튜플 교환
#a, b = 10, 20
#a, b = b, a

#튜플, 함수에서의 활용
#def test():
#    return(10, 20)
#a, b = test()
#print(a)


# 1번째 방법
#def power(item):
#    return item*item
#def under_3(item):
#    return item < 3

# 2번째 방법 : 람다 -> 간단한 함수를 쉽게 선언하는 함수
#power = lambda x: x * x
#under_3 = lambda x: x < 3

#list_input_a = [1, 2, 3, 4, 5]

#map(함수, 리스트), filter(함수, 리스트)
#output_a = map(lambda x: x * x, list_input_a) #이것도 가능
#output_a = map(power, list_input_a) # 그냥 리턴
#print(list(output_a))
#output_b = filter(under_3, list_input_a) # 리턴값이 TRUE인 것
#print(list(output_b))

# 파일 열고 닫기 : 파일 객체 = open(파일경로, 읽기모드) , 파일 객체.close()
# 모드: w (새로쓰기 모드), a(뒤에서 이어쓰기), r(읽기 모드)
#file = open("basic.txt", "w")
#file.write("Hello!")
#file.close()

#이런식으로 하는게 더 효율적
#with open("basic.txt", "w") as file:
#    file.write("Hello!")
#with open("basic.txt", "r") as file:
#    file.read("Hello!")


#랜덤 1000명의 키와 몸무게
#import random
#hanguls = list("가나라다라마바사아자차카타파하")
#with open("basic.txt", "w") as file:
#    for i in range(1000):
#        name = random.choice(hanguls) + random.choice(hanguls)
#        weight = random.randrange(40, 100)
#        height = random.randrange(140, 200)
#        file.write("{}, {}, {}\n".format(name,weight,height))

#with open("basic.txt", "r") as file:
#    for line in file:
#        name, weight, height = line.strip().split(", ")
#        if (not name) or (not weight) or (not height):
#            continue
#        print('\n'.join(["이름 : {}", "몸무게 : {}", "키 : {}"]).format(name,weight,height))
#        print()

# yield -> 함수를 호출해도 함수 내부의 코드가 실행되지 않음
#def test():
#    print("A")
#    yield 1
#    print("B")
#    yield 2
#    print("C")
#output = test()
#print("D")
#a = next(output) #A
#print(a) #1
#print("E")


#numbers = [1, 2, 3, 4, 5]
#print("::".join(map(lambda x: str(x), numbers)))
#print("::".join(map(str, numbers)))

#numbers = list(range(1, 10 + 1))
#print("홀수만 출력")
#print(list(filter(lambda x: x % 2 == 1, numbers)))
#print()
#print("3이상 7미만 출력")
#print(list(filter(lambda  x: 3 <= x < 7, numbers)))
#print()
#print("제곱해서 50미만 출력")
#print(list(filter(lambda  x: x*x < 50, numbers)))
#print()


#try, except
#list_input_a = ["52", "273", "32", "스파이", "103"]
#list_number = []
#for item in list_input_a:
#    try:
#        int(item)
#        list_number.append(item)
#    except:
#        pass
#print("{} 내부에 있는 숫자는".format(list_input_a))
#print("{}입니다".format(list_number))

#try, except, else, finally
#try:
#    number_input_a = int(input("정수 입력"))
#    print(number_input_a)
#except:
#    print("정수를 입력해달라고 했잖아!")
#else:
#    print("예외가 발생하지 않음")
#finally:
#    print("무조건 실행하는 코드에요 어떻게든 끝났네요")

#finally 키워드의 활용
#def write_text_file(filename, text):
#    try:
#        file = open(filename, "w")
#        return
#        file.write(text)
#    except Exception as e:
#        print(e)
#    finally:
#        file.close() #무조건 실행됨

#write_text_file("basic.txt", "hi")

'''
#모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소는 {}이다".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수좀 입력해라")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어남")
    print(type(exception), exception)
except Exception as exception:
    print("미리 파악하지 못한 에러가 발생함")
    print(type(exception), exception)
'''

