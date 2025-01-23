# 1.3.4 리스트 p.30
# 리스트를 사용하여 여러 값을 하나로 묶을 수 있습니다.
a = [1,2,3,4,5] # 리스트 생성
print("a is",a) # a is [1,2,3,4,5]
print("a[0] is",a[0]) # a[0] is 1
print("a[4] is",a[4]) # a[4] is 5
a[4]=99 # a의 4번째 값을 99로 변경
print("a is",a) # a is [1,2,3,4,99]

# 리스트는 슬라이싱 기법도 가능합니다. 
print("a[0:2] is",a[0:2]) # a[0:2] is [1,2]
print("a[1:] is",a[1:]) # a[1:] is [2,3,4,99]
print("a[:3] is",a[:3]) # a[:3] is [1,2,3]
print("a[:-1] is",a[:-1]) # a[:-1] is [1,2,3,4]
print("a[:-2] is",a[:-2]) # a[:-2] is [1,2,3]

# 1.3.5 딕셔너리 
# 딕셔너리는 키와 값을 한 쌍으로 저장할 수 있습니다.
me = {'height':180} # 딕셔너리 생성
print("me['height'] is",me['height']) # me['height'] is 180

# 1.3.6 bool 
# bool은 True, False를 나타냅니다.
hungry = True # 배가 고프다.
sleepy = False # 졸리지 않다.
print("hungry is",hungry) # hungry is True
print("sleepy is",sleepy) # sleepy is False
# 그리고 and 와 or, not 연산자를 사용할 수 있습니다.
print("hungry and sleepy is",hungry and sleepy) # hungry and sleepy is False
print("hungry or sleepy is",hungry or sleepy) # hungry or sleepy is True
print("not hungry is",not hungry) # not hungry is False

