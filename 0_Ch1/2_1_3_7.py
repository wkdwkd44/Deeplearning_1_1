# 1.3.7 if 문 p.32

# 조건에 따라 if 문을 사용할 수 있습니다 .
hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")

# 1.3.8 for 문 p.33
for i in [1, 2, 3]:
    print(i)

# 1.3.9 함수 p.33
# 함수는 def 를 통해 정의할 수 있습니다.
def hello():
    print("Hello World!")

hello()
# 또는 인자를 넣을 수 있습니다 . 
def hello(object):
    print("Hello " + object + "!")
hello("cat")