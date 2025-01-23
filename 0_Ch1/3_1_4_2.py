# 1.4.1 파일로 저장 
# 1.4.2 클래스 p.34
# 클래스를 정의할 수 있습니다.

class Man:
    # 여기서 __init__은 생성자입니다.
    # 생성자는 클래스의 인스턴스가 만들어질 때 한 번만 불립니다.
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()
