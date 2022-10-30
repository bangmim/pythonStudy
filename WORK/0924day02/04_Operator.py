#산술연산자
# +,-,*,/,//,%,**

num1=10
num2=7

print(f'num1+num2={num1+num2}')
print(f'num1-num2={num1-num2}')
print(f'num1*num2={num1*num2}')
print(f'num1/num2={num1/num2}')
print(f'num1//num2={num1//num2}')
print(f'num1%num2={num1%num2}')
print(f'num1**num2={num1**num2}')

# 홀수, 짝수 구할 때 -> 2로 나눈 나머지가 0이면 짝수, 1이면 홀수
# X의 배수를 구할 때 -> X로 나눈 나머지가 0이면 X의 배수이다.

#문자열+문자열 : 문자열 끼리의 연결
print('a'+'b')

#문자열 * 정수 : 정수배 만큼 문자열 반복
print('a'*5)

print('--------------------------------------------')

# 대입연산자
# +,+=,-=,*=,/=,//=,%=,**=

a=10
b=7

a=b
print(f'a=b의 값 : {a}')  #a = 7

a += b  #a=a+b a=7+7 = 14. a=14
print(f'a+=b의 값 : {a}')

a-=b    #a=a-b, 14-7=7. a=7
print(f'a-=b의 값 : {a}')


a*=b    #a=49
print(f'a*=b의 값 : {a}')

a/=b    #a=7
print(f'a/=b의 값 : {a}')

a//=b
print(f'a//=b의 값 : {a}')

a%=b
print(f'a%=b의 값 : {a}')

a**=b
print(f'a/=b의 값 : {a}')

print('-------------------------------------')
x=10
y=5

print(f'x > y: {x>y}')
print(f'x < y: {x<y}')
print(f'x >= y: {x>=y}')
print(f'x <= y: {x<=y}')
print(f'x == y: {x==y}')
print(f'x != y: {x!=y}')

print('-------------------------------------')
#논리 연산자
#and, or, not

#and
print(f'x>y and y>0 : {x>y and y>0}')
print(f'x>y and y>0 : {x<y and y>0}')

#or
print(f'x<y or y>0 : {x<y or y>0}')

#not
a=1
b=0

print(f'not a: {not a}')    #0 False
print(f'not b: {not b}')    #1 True

print('-------------------------------------')
#삼항 연산자
x=10

#result='x는 10 입니다.' if x==10 else 'x는 10이 아닙니다.'
result=True if x==10 else False
print(result)
print('-------------------------------------')
# p.85 (1번)
'''
num = int(input('10~99 사이의 정수를 입력하세요>>>'))
print(f'십의 자리 : {num//10}')
print(f'일의 자리 : {num%10}')
'''
# p.86 (5번)
kor= int(input(f'국어 점수를 입력하세요 >>>'))
eng= int(input(f'영어 점수를 입력하세요 >>>'))
mat= int(input(f'수학 점수를 입력하세요 >>>'))

avg=float((kor+eng+mat)/3)
result='합격' if avg>=80 else '불합격'
print(f'평균은 {avg:.1f}이고, 결과는 {result}입니다.')

#강사님 답안
#result=f'평균은 {avg : .1f}이고, 결과는 합격입니다' avg>=80 else '불합격 입니다'
#print(result)
#f-String 출력법에서 소수점 자리 정하는 법 {변수명 : .1f}






