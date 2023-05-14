from input_util import *
#已修改引入文件中的函数

students = {
}   
def students_add()->str:

    # IDs = students.keys()
    # ID= max(IDs)+1
    # for k in students.items():
    #     print(students[k])
    name = input_str('请输入学生姓名')
    age = input_int('请输入学生年龄：')
    address=input_str('请输入学生地址：')
    excel_result=input_float('请输入学生的excel成绩:')
    python_result=input_float('请输入学生的python成绩:')
    SQL_result=input_float('请输入学生的SQL成绩:')
    IDs = students.keys()
    if len(IDs) == 0:
        ID = 1001
    else:
        ID = max(IDs)+1
    students[ID]=[name,age,address,excel_result,python_result,SQL_result]
    return name

def students_find():
    print( f'{"学生ID".ljust(6)}{"学生姓名".ljust(6)}{"学生年龄".rjust(6)}{"学生地址".ljust(6)}{"excel成绩".ljust(8)}{"python成绩".ljust(8)}{"SQL成绩".rjust(2)}')
    res = ''
    for k, v in students.items():
        res += f'{str(k):<6}{v[0].ljust(10)}{str(v[1]).ljust(10)}{v[2].ljust(13)}{str(v[3]).ljust(8)}{str(v[4]).ljust(8)}{str(v[5]):>8}' + '\n'
    return res

def students_update() -> str:
    # students_find()
    IDs = students.keys()
    s = min(IDs)
    e = max(IDs)
    ID = input_int('请输入要修改的学生序号: ')
    if ID in students:
        n=input_int('1. 修改年龄\n2. 修改成绩\n请选择您:操作：')
        if n==1:
            age = input_int('请输入修改后的学生年龄：')
            students[ID][1]=age
            return f'{students[ID][0]},学生年龄修改成功' 
        elif n==2:
            excel_result=input_float('请输入修改后的学生的excel成绩:')
            python_result=input_float('请输入修改后学生的python成绩:')
            SQL_result=input_float('请输入修改后的学生的SQL成绩:')
        
            students[ID]=[students[ID][0],students[ID][1],students[ID][2],str(excel_result),str(python_result),str(SQL_result)]
            return f'{students[ID][0]},学生信息修改成功' 
    else:
        return '查无此人'

def students_delete() -> str:
    students_find()
    IDs = students.keys()
    s = min(IDs)
    e = max(IDs)
    ID = input_int('请输入要删除的联系人序号: ')
    if ID in students:
        del students[ID]
        return f'已删除该学生信息' 
    else:
        return '查无此人'

def students_album() -> None:
    while True:
        msg = '1. 添加学生信息\n2. 查看学生信息\n3. 修改学生信息\n4. 删除学生信息\n0. 退出程序\n请选择您想要的操作程序:  '
        answer = input_int(msg)
        if answer == 0:
            print('欢迎下次光临')
            break
        elif answer == 1:
            result = students_add()
            print('添加失败' if result is None else f'{result}, 添加成功')
        
        elif answer == 2:
            
            result=students_find()
            print(result)
        elif answer == 3:
            result=students_update()
            print(result)
        else :
            result=students_delete()
            print(result)
        
students_album()

    
