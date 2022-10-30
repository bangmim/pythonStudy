print('My name is {}'.format('James'))
print('My name is {}. I\'m {} years old'.format('James',25))

print('My name is {1}. I\'m {0} years old'.format(25,'James'))    # 번호 지정 가능. 0,1, ...

print('My name is {name}. I\'m {age} years old'.format(name='James',age=25))
# 중괄호에 이름을 정해주고, 그에 대한 변수를 정하면 순서와 상관없이 출력이 가능하다.

print('-------------------------------------------------')
zipcode='06236' #문자열 변수
#print(type(zipcode))

print('우편번호 : {}'.format(zipcode))

address='''서울 특별시 강남구 테헤란로 146 '''

print('주소:{addr}'.format(addr=address))

tel1, tel2, tel3 = '02','538','0021'
print('연락처:{1}-{0}-{2}'.format(tel2,tel1,tel3))

