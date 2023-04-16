# 自定义函数
# def q(n1,n2):
#     return n1+n2
#
# a=float(input('请'))
# b=float(input('请另'))
# c=q(a,b)
# # print(f'和为{c}')
#
def greeting(na,age):
    if age<3:
        a= print(na,'小屁孩')
        return(a)
    elif 3<age<18:
        a= print(na,'没长开的小屁孩')
        return(a)
    elif 18<age<60:
        a= print(na,'屁孩')
        return(a)
    else:
        a= print(na,'老屁孩')
        return(a)

greeting('gougou',2)
greeting('gougou',22)
greeting('gougou',50)
greeting('gougou',100)

# def abc(a,*args):
#         # print(a)
#         # print(args)
#         for i in args:
#             print(i)
# abc('df',6,7,90)
# abc('we',22,43,80)
# abc('fe',66,27,40)
# abc('se',66,17,945)

#
# def abc(a, **args):
#     # print(a)
#     # print(args)
#     for key,value in args.items():
#         print(key,value)
#
# abc('df', f=6, i=7, l=90,u=99)
# abc('we', r=22, p=43, m=80)
# abc('fe', q=66, e=27, g=40)
# abc('se', x=66, v=17, w=945)
#
# def  get_annual_leave(years):
#     if int(years)<5:
#         days=1
#     elif 5<int(years)<10:
#         days=5
#     else:
#         days=7
#     return days
#
# get_annual_leave(years)

# def yunsuan(a,b):
#     shang=a//b
#     yushu=a%b
#     return shang,yushu
# result=yunsuan(5,2)# 赋值并调用,函数内的一个形参就是一把锁，
#                     # 一个实参就是一个钥匙，用的时候要给钥匙进行赋值
# result=yunsuan(7,8)
# print(result)
# # 写出每个月的天数
# def nianfen(year,month):
#     if month in [1,3,5,7,8,10,12]:
#         days=31
#     elif month in [4,6,9,11]:
#         days=30
#     elif month == 2 and year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
#         days=29
#     else:
#         days=28
#     return days
#
#
# year=int(input('请输入任意年份'))
# month=int(input('请输入任意月份'))
# days= nianfen(year,month)
# print(f'{year}年{month}月有{days}天')


# day=0
# year=int(input('请输入任意年份'))
# month=int(input('请输入任意月份'))
# if month in [1,3,5,7,8,10,12]:
#     print(f'{month}月有31天。')
# elif month in [4,6,9,11]:
#     print(f'{month}月有30天')
# elif month==2 and year%4==0 and  year%400==0 or year%100!=0:
#     print(f'{month}月有29天')
# else:
#     print(f'{year}年{month}月有28天')
import random

# red=list(random.randint(1,33))
# for i in range(0,6):
#     if red[i] not in red:
#         red.append(i)
# blue=random.randint(1,16)
# print(red)
# print(blue)