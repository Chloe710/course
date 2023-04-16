#工龄与年假
def gl(year):
    if year<5:
        day=1
    elif 5<year<10:
        day=3
    else:
        day=7
    return day

year=int(input('please input your working years:'))
leave=gl(year)   #必须加这一步调用函数
print(leave)