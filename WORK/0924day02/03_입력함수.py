#name=input('이름을 입력해 주세요 : ')
#print(f'제 이름은 {name}입니다.')
'''
n=int(input('정수를 입력해주세요 : '))
print(n,type(n))
'''

'''
신상정보 (나이, 이름, 키)를 키보드에서 값을 입력받아 변수에 저장하고
출력하기

나이를 입력하세요 : 25
이름을 입력하세요 : 홍길동
키를 입력하세요 :182.5

입력된 이름은 홍길동 입니다.
입력된 나이는 25살 입니다.
입력된 키는 182.5cm입니다.
'''

'''
age = int(input('나이를 입력하세요 : '))
name = str(input('이름을 입력하세요 : '))
height = float(input('키를 입력하세요 : '))
'''
'''
print('입력된 이름은 {}입니다.'.format(name))
print('입력된 나이는 {}살 입니다.'.format(age))
print('입력된 키는 {}cm입니다.'.format(height))
'''
'''
print(f'입력된 이름은 {name}입니다.')
print(f'입력된 나이는 {age}살 입니다.')
print(f'입력된 키는 {height}cm 입니다.')
'''
#age, name, height = input('나이, 이름, 키를 입력해주세요: ').split()
#print(age,name,height)
'''
num1, num2,num3 = map(int, input('정수1, 정수2, 정수3을 입력해주세요 : ').split())
print(type(num1))   #int
'''

#회원가입 프로그램
'''
사용자에게
id
pw
name
age
gender
를 입력받아 변수에 저장하고
저장한 값들을 다음과 같이 출력하는 프로그램 구현
'''


Id=str(input(f'id를 입력해주세요 : '))
pw=str(input(f'pw를 입력해주세요 : '))
name=str(input(f'이름을 입력해주세요: '))
age=int(input(f'나이를 입력해주세요: '))
gender=str(input(f'성별을 입력해주세요: '))
           
print('☆★☆★회원정보☆★☆★')
print(f'아이디 : {Id}')
print(f'비밀번호 : {pw}')
print(f'이름 : {name}')
print(f'나이 : {age}')
print(f'성별 : {gender}')
print('☆★☆★☆★☆★☆★☆★')

