
# 1.5.5 브로드캐스트 p.39
# 4번 파일에서 보았듯 브로드 캐스트는 행렬 크기가 서로 달라도 
# 어느정도 연산이 가능하도록 도와줍니다. 
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print("A is")
print(A)
print("B is")
print(B)
print("A*B is:")
print(A*B)

# 1.5.6 원소 접근 p.40
X = np.array([[51,55],[42,41],[31,37]])
print("X is")
print(X)
print("X[0] is",X[0]) # [51 55]
print("X[0][1] is ",X[0][1]) # 55
# 넘파이 배열은 인덱스를 지정하여 원소에 접근할 수 있습니다.

# for 문으로도 접근할 수 있습니다 . 
for row in X:
    print(row)

#flatten() 메서드를 사용하면 다차원 배열을 1차원 배열로 변환할 수 있습니다.
Y = X.flatten()
print("Y is",Y)
for i in Y:
    print(i)

# 일부 인덱스로 접근하고 싶다면, 인덱스를 배열로 지정하면 됩니다.
print(X[np.array([1,0,1])]) # 1행, 0행, 1행 순으로 출력 
print(Y[np.array([0,2,4])]) # 0,2,4번째 원소 출력

# 해당 기법을 응용하여 조건문으로 만족하는 원소만 추출할 수 있습니다.
print(Y>40) # [ True  True  True  True  False False]
print(Y[Y>40]) # [51 55 42 41]