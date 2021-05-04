PI = 3.141592

def number_input():
    output = input("숫자 입력: ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

#활용 예 -> 외부에서 불러오면 실행x , 여기서(메인)으로 하면 실행o
if __name__ == "__main__":
    print(get_circle_area(3))