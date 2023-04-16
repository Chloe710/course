#年假天数
def get_annual_leave(years):#没有将days作为函数的参数，是因为days的值是由函数内部的逻辑判断得出的。
    if years<5:                        # 而不是由函数调用者提供的参数
        days=1
    elif 5<years<10:
        days=5
    else:
        days=7
    return days #返回一个值，只能被函数的调用者使用，其他的代码无法直接获取这个值。
# return语句可以让函数返回一个值，而不需要使用print()函数进行输出。
# 在这个例子中，函数get_annual_leave()使用return语句将计算结果返回给调用者，
# 而调用者可以使用这个返回值进行后续的处理或输出。
# 因此，在最后一行代码中，使用print()函数输出结果只是为了将结果显示在屏幕上，以方便用户观察，而不是必需的操作。
# 需要注意的是，return语句可以让函数返回一个值，
# 但是这个值只能被函数的调用者使用，其他的代码无法直接获取这个值。
# 如果需要在函数内部将计算结果输出到屏幕上或者保存到文件中，
# 可以使用print()函数或其他输出函数进行输出，或者将计算结果保存到文件或数据库中，以供其他程序使用。
g=int(input('请输入工龄'))
days=get_annual_leave(g)  # 1.括号里这里是在调用参数，将years的值赋值给input的内容，
   #只能被调用者使用         # 2.days是将函数返回的结果赋值
print(f'您的年假为{days}天数')
#practise
# def nianjia(years):
#     if years<5:
#         days=1
#     elif 5<years<10:
#         days=3
#     else:
#         days=5
#     return days
#     #定义完成
# # 开始调用
# g=int(input('请输入工龄：'))
# days=nianjia(g)
# print(f'您的年假为{days}天')
