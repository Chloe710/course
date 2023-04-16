print('hello,world!')
print('我现在要玩转义字符了\n记住是要用反斜杠')
print('\t我现在要玩转义字符了,记住是要用反斜杠,转义字符要在引号内放置')
print('我现在要玩转义字符了,记住是要用反斜杠,转义字符要在引号内放置',end='')
print('hello,world!')
# ctrl/是转注释，单行注释
print('我现在要玩转义字符了,\b记住是要用反斜杠,转义字符要在引号内放置***')
print('我现在要玩转义字符了,\0记住是要用反斜杠,转义字符要在引号内放置***')
'''
是多行注释
是多行注释
是多行注释
'''

'''
我现在要玩转义字符了
我现在要玩转义字符了
我现在要玩转义字符了
'''
import keyword
print(keyword.kwlist)
aa,bb,cc='diyi','dier','disan'
print('username'+aa)
print('用户名为'+aa)
print('用户名为',aa)

company='北大青鸟教育科技有限公司'
name='张丽：'
namevalue='课程设计师'
tel='手机：'
telvalue='13811111111'
phone='电话：'
phonevalue='010-12345678'
adress='地址：'
adressvalue='北京市海淀区成府路207号'
print('--------------------------------')
print(f'{company}\n{name}{namevalue}\n{tel}{telvalue}\n{phone}{phonevalue}\n{adress}{adressvalue}')
print('--------------------------------')

card1,card2,card3,card4,card5,card6=1,2,3,4,5,6
print(card1,card2,card3,card4,card5,card6)
print(int(card1)+int(card2)+int(card3)+int(card4)+int(card5)+int(card6))
#输出结果： 123456   21
