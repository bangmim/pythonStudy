#형변환

int(1.9) #(실수>)정수형 변환
print(int(1.9))
#실수 > 정수로 변환 시 데이터 크기가 다르기 때문에 실수의 소수점 아래 숫자는 유실된다.
#데이터 타입마다 크기가 다르다

#int > 4byte
#float > 8byte
#bool > 1byte
#str > 쓰는 만큼 데이터 차지

#True, False를 사용할 때는 첫 글자를 무조건 대문자로 사용해야 한다.
print(int(True)) #프로그래밍에서 참 : 1 , 거짓 : 0
print(int(False)) 
print(int('100')) #문자열 100을 정수 100으로 변환 
print(type('100')) #type : 어떤 자료형인지 알려준다.
print(type(int('100'))) # 함수가 여러개 묶여있으면 가장 안쪽 함수부터 풀이가 된다.
                        # -> int('100')이 숫자형으로 변환이 되었구나 알 수 있음.
print('-----------------------------------------------------------------------------------------')
print(float(1)) #1.0
print(type(float(1)))
print(float(True)) #1.0
print(type(float(True)))
print(float(False)) #0.0
print(float('3.14')) #문자열이 실수형으로 변환
print(type(float('3.14')))
print('-----------------------------------------------------------------------------------------')
print(bool(1))
print(bool(0))
print(bool('')) #비어있는 문자열 > False로 판단
print(bool(None))#False로 판단

num=None; #변수는 만들고 싶은데 당장 값을 넣고 싶지는 않을 때, 값이 없는 경
print('-----------------------------------------------------------------------------------------')
print(str(100))
print(type(str(100)))
print(str(True))
print(type(str(True)))
print(str(3.14))
print(type(str(3.14)))
