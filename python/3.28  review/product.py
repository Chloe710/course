# # for i in range(1,10):
# #     for j in range(1,10):
# #         print(f'{i}*{j}={i*j}\t',end='')
# #     print()
# name=['a','b','c','d','e']
# tel=['137','136','138','156','153']
#
# while True:
#     A=int(input('请选择你的操作：1 新建联系人 2 查看联系人 3 修改联系人 4 删除联系人 0 退出\n'))
#     if A==1:
#         newn=input('请新建联系人姓名:')
#         newt=input('请新建联系人电话:')
#         name.append(newn)
#         tel.append(newt)
#     elif A==2:
#         print('-----------通讯录-------------')
#         print('姓名', '\t', '电话')
#         for n, t in zip(name, tel):
#             print(n, '\t\t', t)
#         print('-----------------------------')
#     elif A ==3:
#         mendn = input('请输入修改联系人姓名：')
#         mix = None
#         for i in range(0, len(name)):
#             if name[i] == mendn:
#                 mix = i
#                 mendt = input('请输入新联系人电话：')
#                 tel[mix] = mendt
#                 break
#         if mix is not None:
#             print('修改完成！')
#         else:
#             print('员工信息未找到。')
#
#     elif A == 4:
#         deln = input('请输入删除联系人姓名：')
#         rep = None
#         for i in range(0, len(name)):
#             if name[i] == deln:
#                 rep = i
#                 del name[rep]
#                 del tel[rep]
#                 break
#         if rep is not None:
#             print('联系人已删除')
#         else:
#             print('员工信息未找到。')
#
#     elif A==0:
#         print('程序结束！')
#         break
#     else:
#         print('请重新输入：')


