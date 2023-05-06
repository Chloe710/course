# 自制通讯录
# 定义一个二维列表保存姓名和电话信息
# 一维：每个人的姓名和电话
# 二维：每个人的信息

import re

users = [
    ['尼古拉斯·赵四', '130-1234-5678'],
    ['约翰尼·宋小宝', '131-0001-1000']
]

# 循环实现多次选择
while 1:
    # 接收一个数字作为选项
    key = input('1. 新建联系人\n2. 查看联系人\n3. 修改联系人\n4. 删除联系人\n0. 退出\n请选择: ')
    if key.isdigit():
        key = int(key)
        if 0 <= key <= 4:
            if key == 0:
                print('欢迎下次使用')
                break
            elif key == 1:
                name = input('请输入姓名: ')
                regex = '^(\+86[- ])?1[3-9][0-9]{9}$'
                while 1:
                    phone = input('请输入手机号码: ')
                    if re.match(regex, phone) is not None:
                        phone = phone[::-1]
                        phone = phone[:4] + '-' + phone[4: 8] + '-' + phone[8:]
                        phone = phone[::-1]
                        users.append([name, phone])
                        print(f'{name}添加成功')
                        break
                    else:
                        print('手机号有误')
                pass
            elif key == 2:
                pass
            elif key == 3:
                pass
            elif key == 4:
                pass
            print('='*30)
        else:
            print('输入选择有误')
    else:
        print('您输入的不是数字')

print(users)