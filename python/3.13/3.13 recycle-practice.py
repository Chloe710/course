#幸运数字
# import random
# award=random.randint(0,9)
# guess=(input('请输入四位有效数字：'))
# if guess.isdigit() and guess[0]!='0'and len(guess)==4:
#     # if int(guess) // 100 % 10 != 0 :
#         if int(guess[1])==award:
#             print(f'百位数字为：{guess[1]}中奖数字为{award}' )
#             print('恭喜您中奖了！')
#
#         else:
#             print(f'百位数字为：{guess[1]}中奖数字为{award}')
#             print('您没中奖！')
#
# else:
#     print('您的输入不正确，请重新输入：')
#求10以内奇数
# i=1
# while i<=10:
#     if i % 2 ==1:
#         print(i)
#     i=i+1
#求20以内偶数和
# i=1
# sum=0 #必须要在前面进行赋值，之后才能运算，
# while i<=20:
#     if i % 2 ==0: #这一步判断为偶数
#         sum=sum+i # 这里
#     i=i+1
# print(f'所有偶数的和为{sum}')

#求偶数平均数
# i=1
# sum=0
# count=0
# while i<=100:
#     if i%2!=0:#满足这个条件为偶数
#         sum=sum+i
#         count=count+1
#     i=i+1
#     # print(sum)
#     # print(count)
# avrsum=sum/count
# print(avrsum)
#
#
# 求100以内所有数之和
# i=0
# sum=0
# for i in range(1,101):
#     sum+=i#数列所有值之和，所以每次循环加一个数，不是加1
#     i += 1
#
# print(sum)

#求极值
# num=int(input('请'))

# while True:#也可以while num !=’0‘
#     num = int(input('请'))
#     if num==0:
# #         break
# list_ = []
# input_num = int(input('请输入一个整数(输入0结束):'))
# # while input_num != 0:
# list_.append(input_num)
# print(list_)


# list_=[]
# input_num=int(input('请'))
# while input_num!=0:
#     list_.append(input_num)#dian 是默认程序 点就是的
#     print(list_)
#     input_num = int(input('请'))
# print(max(list_),min(list_))


#九九乘法表
#
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f'{x}*{y}={x*y}',end=' ')#这个空格在这表示一个算式空格
#     print()#print 默认带空格，这个空值必须夹在第一个for循环里面，表示行换行

# 鸡兔同笼 二元一次方程
# x+y=3600
# 2x+4y=11000
# for x in range(3600):
#     y=3600-x
#     if y*2==11000-3600*2:
#         print(x,y)
#挑出5的倍数
# for i in range(0,100):
#     if i % 5==0:
#         print(i)
#挑出偶数
# for i in range(0,100):
#     if i % 2==1:
#         continue
#
#     print(i)
# #
#写出每个月的天数
# day=0
# year=int(input('请输入任意年份'))
# month=int(input('请输入任意月份'))
# if month in [1,3,5,7,8,10,12]:
#     print(f'{month}月有31天。')
# elif month in [4,6,9,11]:
#     print(f'{month}月有30天')
# elif month==2 and year%4==0 and  year%400==0:
#     print(f'{month}月有29天')
# else:
#     print(f'{year}年{month}月有28天')
#自动跳出星期
# while 1:
#     num=int(input('请输入数字1-7（输入0结束）'))
#     if num ==1:
#         print('MON')
#         continue
#     elif num==2:
#         print('TUE')
#         continue
#     elif num==3:
#         print('WED')
#         continue
#     elif num==4:
#         print('THUR')
#         continue
#     elif num==5:
#         print('FRI')
#         continue
#     elif num == 6:
#         print('SAT')
#         continue
#     elif num==7:
#         print('SUN')
#         continue
#     elif num>7:
#         print('请重新输入：')
#         continue
#     else:
#         print('程序结束！')
#         break

#翻转
i='6830575629474'
print(i[::-1])
print(''.join(reversed('6830575629474')))


