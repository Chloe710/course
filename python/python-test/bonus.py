# def wt(month):
#     if month<6:
#         bonus=500
#     elif 6<month<12:
#         bonus=(120*month)
#     else:
#         bonus=(180*month)
#     return(bonus)
# def aword():
#     staff=input('请输入您的名字：')
#     month=int(input('请问您一共入职了多少月份：'))
#     print(f'{staff}来了{month}个月，获得奖金{wt(month)}')
# aword()
def my_list(num1,num2):
    global m1
    global m2
    global m3
    your_list=num1+num2
    return (your_list)
m1=my_list(num1=(1,2),num2=(3,))
m2=my_list(num1=(1,2),num2=(3,4))
m3=my_list(num1=(1,2,3,6,9,16),num2=(23,35,79,88,90))
print(m1)
print(m2)
print(m3)
def l_median(yourlist):
    median = 0
    if len(yourlist) % 2 == 0:
        med_index = len(yourlist) // 2-1
        median = (yourlist[med_index]+yourlist[med_index+1])/2
    else:
        med_index = (len(yourlist) // 2)
        median = yourlist[med_index]
    return (median)
print(l_median(yourlist=m1))
print(l_median(yourlist=m2))
print(l_median(yourlist=m3))
