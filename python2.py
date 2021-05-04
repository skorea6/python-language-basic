# <312pg , 모듈>

# 1. math 모듈
# 데이터베이스에 실수를 정수로 -> 올림할때 : ceil(x) , 내림할때: floor(x)
# 반올림할때: round(x) 소수점이 5일때, 정수가 짝수면 내리고, 홀수면 올림
#import math
#print(math.sin(1))

# from 구문
#from math import sin, cos, tan, floor, ceil
#print(tan(1))

# as 구문
#import math as m
#print(m.sin(1))


# 2. random 모듈
#import random
#print(random.uniform(10, 20)) # 10~20까지 랜덤 숫자 1개, float
#print(random.randrange(10, 20)) # 10~20까지 랜덤 숫자 1개, int
#print(random.choice([1, 2, 3, 4, 5])) # 리스트 내부에 있는 요소 랜덤 1개 선택
#print(random.shuffle([1, 2, 3, 4, 5])) # 리스트 요소들을 랜덤하게 섞음
#print(random.sample([1, 2, 3, 4, 5], k=2)) # 리스트 요소들 중에 2개를 랜덤히 뽑음


# 3. sys 모듈
#import  sys
#print(sys.argv)
#print(sys.getwindowsversion())
#print(sys.copyright)
#print(sys.version)


# 4. os 모듈
#import os
#print("운영체제: ", os.name)
#print("폴더: ", os.getcwd())
#print("폴더 내부요소: ", os.listdir())

#os.mkdir("hello") #디렉토리 생성
#os.rmdir("hello") #디렉토리 삭제

#파일 생성 후 파일 이름 변경
#with open("original.txt", "w") as file:
#    file.write("hello0")
#os.rename("original.txt", "new.txt")

#os.remove("new.txt") #파일 제거
#os.system("ipconfig") # 시스템 명령어 실행


# 5. datetime 모듈
#import datetime
#now = datetime.datetime.now()
#print(now.month)
#print(now.strftime("%Y-%m-%d %H:%M:%S"))
#print(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#after = now + datetime.timedelta(hours=1) #[1] 날짜,시간 추가 (weeks,days,hours,minutes,seconds)
#after2 = now.replace(year=(now.year + 1)) #[2] 2번째 방법 (연도를 바꿀 수 있는 유일한 함수)


# 6. time 모듈
#import time

#print("5초 정지")
#time.sleep(5)
#print("종료됨")


# 7. urllib 모듈
#from urllib import request  # urllib에 있는 request 가져오기
#target = request.urlopen("https://google.com")
#print(target.read())

# 예시) 현재 폴더 내부에 있는 모든 파일 탐색 (재귀함수 이용)
#import os

#def read_folder(path):
#    output = os.listdir(path)
#    for item in output:
#        if os.path.isdir(item):
#            read_folder(item)
#        else:
#            print("파일: ", item)

#read_folder(".")


# 332pg, 외부 모듈

# 1. BeautifulSoup4 모듈
#from urllib import request
#from bs4 import BeautifulSoup

#target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#soup = BeautifulSoup(target, "html.parser")

#for location in soup.select("location"):
#    print("도시: ", location.select_one("city").string)
#    print()


# 2. Flask 모듈
#from flask import Flask
#from urllib import request
#from bs4 import BeautifulSoup

#app = Flask(__name__)
#@app.route("/")

#def hello():
#    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#    soup = BeautifulSoup(target, "html.parser")

#    output = ""
#    for location in soup.select("location"):
#        output += "<h3>{}</h3>".format(location.select_one("city").string)
#        output += "날씨: {}<br/>".format(location.select_one("wf").string)
#        output += "최저/최고 기온: {}/{}"\
#            .format(location.select_one("tmn").string,\
#                    location.select_one("tmx").string)
#        output += "<hr/>"
#    return output


# 모듈 만들기
#import test_module as test

#radius = test.number_input()
#print(test.get_circumference(radius))
#print(test.get_circle_area(radius))


# 패키지 만들기
#import test_package.module_a as a  # ./test_package/module_a.py
#import test_package.module_b as b
#print(a.variable_a)
#print(b.variable_b)

#from test_package import *
#print(module_a.variable_a)
#print(module_b.variable_b)


# 인터넷 이미지 저장
#from urllib import request

#target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
#output = target.read()
#print(output)

#file = open("output.png", "wb") #write binary 모드 | 이 외에도 read binary: rb 도 있음
#file.write(output)
#file.close()



# Class
"""
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

students = [
    Student("윤인성", 35, 48, 98, 91),
    Student("윤아린", 95, 98, 98, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())
"""

"""
# isinstance(인스턴스, 클라스)
class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
"""

"""
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __ge__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("윤인성", 35, 48, 98, 91),
    Student("윤아린", 95, 98, 98, 92)
]

student_a = Student("윤인성", 35, 48, 98, 91)
student_b = Student("윤아린", 32, 48, 98, 80)

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

print("student_a > student_b = ", student_a > student_b)
"""

"""
#TypeError 발생시키기
class Student:
    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다")
        return self.get_sum() == value.get_sum()
    #생략
    
student_a == 10
"""

"""
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다".format(Student.count))

students = [
    Student("윤인성", 35, 48, 98, 91),
    Student("윤아린", 95, 98, 98, 92)
]

#클래스 내부와 외부에서 클래스 변수에 접근할 때는 모두 <클래스이름.변수이름> 을 사용!!
print("현재 생성된 총 학생수는 {}명입니다.".format(Student.count))
"""

"""
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("---학생 목록---")
        print("이름", "총점", "평균", sep="\t")
        for student in cls.students:
            print(str(student))
        print("----------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

Student("윤인성", 87, 98, 88, 95)
Student("윤이성", 37, 98, 28, 95)
Student("윤삼성", 57, 98, 78, 95)

Student.print()
"""

"""
# 프라이빗 변수 : 변수를 외부에서 사용하는 것을 막고 싶을때 __<변수이름>
# 게터와 세터 : 프라이빗 변수의 값을 추출하거나 변경할 목적으로, 간접적으로 속성에 접근하도록 해주는 함수
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터를 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print(circle.get_circumference(), circle.get_area())
print(circle.get_radius())
circle.set_radius(2)
print(circle.get_circumference(), circle.get_area())
"""

"""
# 데코레이터를 사용한 게터와 세터
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터를 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다")
        self.__radius = value

circle = Circle(10)
print(circle.radius)
circle.radius = 2
print(circle.radius)

print("강제 예외")
circle.radius = -2
"""

"""
# 상속
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 메소드가 출력 되었습니다")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init__ 메소드가 출력 되었습니다")

child = Child()
child.test()
print(child.value)
"""

"""
# 상속 예시
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value
    def __str__(self):
        return self.message
    def print(self):
        print("<오류 정보>")
        print("메시지: ", self.message)
        print("값: ", self.value)

try: #예외 발생 시키기
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()
"""

