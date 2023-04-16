# # 通讯录
# name=['a','b','c','d','e']  #两个列表的元素要一一对应，这是前提
# tel=['137','136','138','156','153']
#
# while True: #可以改：1，字符串，空的列表和字典
#     A=int(input('请选择你的操作：1 新建联系人 2 查看联系人 3 修改联系人 4 删除联系人 0 退出\n'))
#     if A==1:#添加新元素，用append
#         newn=input('请新建联系人姓名:')
#         newt=input('请新建联系人电话:')
#         name.append(newn) #增加语法：列表-.-append-(变量名)
#         tel.append(newt)
#     elif A==2: #注意语法，对齐
#         print('-----------通讯录-------------')
#         print('姓名', '\t', '电话')
#         for n, t in zip(name, tel):# 在遍历的过程中，同时遍历多列表，
#                                   # 先用变量说分别在那个列表中，用zip(列表一，列表二)
#             print(n, '\t\t', t)    #一个中午字符两个字节
#         print('-----------------------------')
#     elif A ==3: #修改元素，要先寻找
#         mendn = input('请输入修改联系人姓名：') #先赋值，
#         mix = None #设计标签
#         for i in range(0, len(name)): #开始遍历，注意这里的尾巴，
#                                      # 绝对不能提前na_count赋值len(name),
#                                       # 否则增加元素之后不会被查找到，直接用函数len()）
#             if name[i] == mendn: #输入值和现有值进行匹配，找到他的顺序号
#                 mix = i            #输入值和顺序号相匹配
#                 mendt = input('请输入新联系人电话：') #同时赋值电话
#                 tel[mix] = mendt   # 电话匹配
#                 break # 停止遍历，要在if内部进行，否则会重复搜索不能进行while循环里的内容
#         if mix is not None:  #  确保mix这个空值现在已经有内容，已经被输入值传参
#             print('修改完成！')
#         else:
#             print('员工信息未找到。')
#
#     elif A == 4:# 删除用del函数，和pop的语法不同，语法为： del
#         deln = input('请输入删除联系人姓名：')
#         rep = None
#         for i in range(0, len(name)):
#             if name[i] == deln:
#                 rep = i
#                 del name[rep]
#                 del tel[rep]
#                 break
#         if rep is not None:,
#             print('联系人已删除')
#         else:
#             print('员工信息未找到。')
#
#     elif A==0:
#         print('程序结束！')
#         break
#     else:
#         print('请重新输入：')
#
na=[a,b,c,d,e]
tel=[1,2,3,4,5]

while True:
    a=int(input('请'))
    if a==1:
        newn=input('p creat  the new name ')
        newt=input('p creat the new tel ')
        na.append.newn
        tel.append.newt
    elif a==2:
        for i in na[0, len(na)]:





        #

