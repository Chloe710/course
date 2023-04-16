# # # #添加与删除变量
# # # em=['张三','李四','王五','赵六']
# # # sal=[4000,5000,6000,7000]
# # # for e,s in zip(em,sal):
# # #     # print(e,'\t',s)
# # #     pass
# # # em.append('陈大') #默认在结尾增加
# # # sal.append(7900)
# # # del em[3] #删减在前面加del不用加符号，直接加列表
# # # del sal[3]
# # # print(em)
# # # # print(sal)
# # # 在列表中查找算法
# # # em=['张三', '李四', '王五', '陈大']
# # # sal=[4000, 5000, 6000, 7900]
# # # emp_count=len(em) #要找到列表的总长度，为了一会在索引中寻找值的时候从头到尾找一遍。
# # # del_index=None #none 是在列表中绝对不会出现的索引，相当于做一个记号，
# # #                # 在找到目标后做一个记号，因为还不知道是啥，所以赋值为None。
# # # for i in range(0,emp_count): #在列表里找到目标
# # #     if em[i] =='陈大': #给出寻找的线索：名字是陈大 一定要写成，在em[]列表中的i，
# # #         del_index=i  #把目标的序号赋值给记号
# # #         break
# # # 为了验证是否真正找到这个值，
# # # if del_index is not None: # 做记号的那个值如果真的存在，即不为空值。不加这一步程序报错为，没有空值。
# # #     em.pop(del_index) #格式是 列表.pop(索引)
# # #     sal.pop(del_index)#
# # #     print('陈大已离职')
# # # else:
# # #     print('没有找到陈大的员工记录')
# # # # #
# # # # #张三涨工资为6000
# # # em=['张三', '李四', '王五', '陈大']
# # # sal=[4000, 5000, 6000, 7900]
# # #
# # # em_count=len(em)
# # # ra_index=None
# # # for i in range(0,em_count):
# # #     if em[i]=='张三':
# # #         ra_index=i
# # #         break
# # # if ra_index is not None:
# # #     sal[ra_index]=5000
# # #     print(em)
# # #     print(sal)
# # # else:
# # #     print('无法找到张三的员工信息')
# # #
# # #
# # # #
# # # #
# # # em=['张三', '李四', '王五', '陈大']
# # # sal=[4000, 5000, 6000, 7900]
# # # #
# # # # a=em.pop()
# # # # print(a)
# # #
# # # del em[1:]
# # # print(em) mendt = input('请输入新联系人电话:')
name=['a','b','c','d','e']
tel=['137','136','138','156','153']

while True:
    A=int(input('请选择你的操作：1 新建联系人 2 查看联系人 3 修改联系人 4 删除联系人 0 退出\n'))
    if A==1:
        newn=input('请新建联系人姓名:')
        newt=input('请新建联系人电话:')
        name.append(newn)
        tel.append(newt)
    elif A==2:
        print('-----------通讯录-------------')
        print('姓名', '\t', '电话')
        for n, t in zip(name, tel):
            print(n, '\t\t', t)
        print('-----------------------------')
    elif A ==3:
        mendn = input('请输入修改联系人姓名：')
        mix = None
        for i in range(0, len(name)):
            if name[i] == mendn:
                mix = i
                mendt = input('请输入新联系人电话：')
                tel[mix] = mendt
                break
        if mix is not None:
            print('修改完成！')
        else:
            print('员工信息未找到。')

    elif A == 4:
        deln = input('请输入删除联系人姓名：')
        rep = None
        for i in range(0, len(name)):
            if name[i] == deln:
                rep = i
                del name[rep]
                del tel[rep]
                break
        if rep is not None:
            print('联系人已删除')
        else:
            print('员工信息未找到。')

    elif A==0:
        print('程序结束！')
        break
    else:
        print('请重新输入：')

