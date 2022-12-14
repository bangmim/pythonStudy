#정수형 타입
print(100)
print(200)

#논리형 타입
print(True)
print(False)

#실수형 타입
print(3.14)
print(1.3)

#문자열 타입
print('hello Python',end = ' ')
#end ='띄어쓰기' 줄바꿈 적용이 안된다(아래 문장과 바로 이어서 출력된다)
print("hello world")

#print는 여러개의 값을 한번에 출력할 수 있다.
print(100,200,300,400,500)  #기본값: 공백
print(100,200,300,400,500, sep=',')
#sep ='' 내가 원하는 값으로 구분을 줄 수 있다.
print(100,200,300,400,500, sep='*')
print(100,200,300,400,500, sep='/')

print("---------------------------------------------------------------------------------------------")
#출력함수 내에서 간단한 연산이 가능하다
print(1+1)
print(1.5+3) # 실수 + 정수 = 4.5 (실수로 표현)
print(1-2)
print(2.5-1) # 실수-정수 =1.5(실수)
print(2*5)
print(1.5*8) # 실수 * 정수 = 12.0 (실수로 표시)

print(4/2) # 정수/정수 = 2.0 실수
print(type(4/2))

print(2**5) # 정수의 제곱 -> 정수
print(2.5**2) # 실수의 제곱 -> 실수

#str(문자열 연산)
print('R'+'E'+'D') # 문자열 끼리의 연산은 글자를 합친다
print('1'+'1'+'1')
print('안녕하세요'+'1')
#print('안녕하세요'+1) # 오류

print('안녕하세요'*10) # 문자열 * 정수 -> 문자열이 정수배 만큼 출력된다

print('') # 빈 문자열
print('    ') # 공백이 있는 문자열

print("---------------------------------------------------------------------------------------------")
print('hello \'world\'')
print('hello "world"') 
print("hello 'world'") 
print("hello \"world\"")
print('*\n**\n***')
print('이름\t연락처')
print('제시카\t02-123-4567')
print('마틴\t010-8765-4321')

print("---------------------------------------------------------------------------------------------")
#print('%d' %데이터 or 변수(형식 기호에 맞는 데이터 값을 입력해야한다))
print('%d' %100)
print('%.2f' %3.14) #소수점 자릿수 지정하여 표시 가능
print('%s' %"홍길동")


print('%d, %.2f, %s' %(100, 3.143546, "홍길동"))

'''
신상 정보 (나이, 이름, 키)를 갖는 변수를 만들고 형식 기호를 이용해서 출력하기
'''
#변수와 데이터 입
age=25
name='김카이'
height=165

print('내 나이는 %d세 입니다.' %age)
print('내 이름은 %s 입니다.' %name)
print('내 키는 %.1fcm 입니다.' %height)






