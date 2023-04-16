# #写出每个月的天数
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

def tl(year,month):
    if month in [1,3,5,7,8,10,12]:
        day=31
    elif month in [4, 6, 9, 11]:
        days=30
    elif month == 2 and year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
        days=29
    else:
        days=28
    return days
year=int(input('please input a year'))
month=int(input('please input a month'))
chaxun=tl(year,month)
print(f'{year}年{month}月有{chaxun}天')