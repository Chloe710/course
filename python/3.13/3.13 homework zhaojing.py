# 写出每个月的天数
day=0
year=int(input('请输入任意年份'))
month=int(input('请输入任意月份'))
if month in [1,3,5,7,8,10,12]:
    print(f'{month}月有31天。')
elif month in [4,6,9,11]:
    print(f'{month}月有30天')
elif month==2 and year%4==0 and year%100!=0 or year%400==0:
    print(f'{month}月有29天')
else:
    print(f'{year}年{month}月有28天')
# 自动跳出星期
# # #
# # # while 1:
# #     num=int(input('请输入数字1-7（输入0结束）'))
# #     if num ==1:
# #         print('MON')
# #
# #     elif num==2:
# #         print('TUE')
# #
# #     elif num==3:
# #         print('WED')
# #
# #     elif num==4:
# #         print('THUR')
# #
# #     elif num==5:
# #         print('FRI')
# #
# #     elif num == 6:
# #         print('SAT')
# #
# #     elif num==7:
# #         print('SUN')
# #
# #     elif num>7:
# #         print('请重新输入：')
# #
# #     else:
# #         print('程序结束！')
# #         break
# #简化版 in
# num1=[1,2,3,4,5,6,7]
# weekday=['MON','TUE','WED','THER','FRI','SAT','SUN']
# # for i,j,in zip(num1,weekday):
#     num=int(input('请输入数字1-7（输入0结束）'))
#     if num ==i:
#         print(j)
#     elif num>7:
#         print('请重新输入：')
#     else:
#         print('程序结束！')
#         break
#
#     # elif num==2:
#     #     print('TUE')
#     #
#     # elif num==3:
#     #     print('WED')
#     #
#     # elif num==4:
#     #     print('THUR')
#     #
#     # elif num==5:
#     #     print('FRI')
#     #
#     # elif num == 6:
#     #     print('SAT')
#     #
#     # elif num==7:
#     #     print('SUN')
#     #
#     # elif num>7:
#     #     print('请重新输入：')
#     #
#     # else:
#     #     print('程序结束！')
#     #     break
# #翻转
# # i='6830575629474'
# # print(i[::-1])
# # print(''.join(reversed('6830575629474')))