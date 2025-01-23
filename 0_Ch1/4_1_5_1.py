# 1.5 넘파이
# 1.5.1 넘파이 가져오기 p.36
import numpy as np
# 위와 같이 쓰면 넘파이를 np라는 이름으로 사용할 수 있다.
# 넘파이는 수치 계산을 위한 라이브러리이다.

# 1.5.2 넘파이 배열 생성하기 p.37
x = np.array([1.0, 2.0, 3.0])
print("x is",x) # [1. 2. 3.]
print("x type is",type(x)) # <class 'numpy.ndarray'>
# 넘파이 배열을 만들 때는 np.array() 메서드를 사용한다.
# 넘파이 배열은 넘파이의 ndarray 클래스의 객체이다.

# 1.5.3 넘파이의 산술 연산 p.37
