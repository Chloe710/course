import re
users=[
    ['尼古拉斯·赵四', '130-1234-5678'],
    ['约翰尼·宋小宝', '131-0001-1000']
]
while True:
    A = input('请选择你的操作：1 新建联系人 2 查看联系人 3 修改联系人 4 删除联系人 0 退出\n')
    if A.isdigit():
        A=int(A)
        if 0<=A<=4:
            if A==0:
                print('Welcome next time!')
                break
            elif A==1:
                newn = input('请新建联系人姓名:')
                regex='^(\+86[- ])?1[3-9][0-9]{9}$'
                while 1:
                    newt = input('请输入新建联系人电话:')
                    if re.match(regex,newt) is not None:
                        newt = newt[::-1]
                        newt = newt[:4] + '-' + newt[4: 8] + '-' + newt[8:]
                        newt = newt[::-1]
                        users.append([newn, newt])
                        print(f'{newn}添加成功')
                        break
                    else:
                        print('This is a wrong number.')
                pass
            elif A==2:
                C=input('1.查看所有联系人\n2.查看指定联系人')
                if C.isdigit():
                    C=int(C)
                    if C==1:
                        print('姓名'.ljust(15),'电话'.center(15))
                        for u in users:
                            print(u[0].ljust(15),u[1].center(15))
                        pass
                    elif C==2:
                        name=input('请输入查看联系人的姓名：')
                        for i in users:
                            if name in i:
                                print(name,i[-1])
                                break
                        else:
                            print('查无此人')
                pass
            elif A==3:
                name=input('please input the name you want to edit:')
                for i in users:
                    if name in i:
                        while 1:
                            phone=input('Please input the number you`ve edited:')
                            regex='^(\+86[- ])？1[3-9][0-9]{9}$'
                            if re.match(regex,phone) is not None:
                                i[-1]=phone
                                break
                            else:
                                print('This is a wrong number!')
                        break
                else:
                    print('查无此人')

            elif A == 4:
                name=input('please input the name you want to delete')
                for u in users:
                    if name in u:
                        users.remove(u)
                        print('done')
                        break
                else:
                    print('查无此人')
                pass
            print('='*30)
        else:
            print('输入有误')
    else:
        print('This is not digit.')
