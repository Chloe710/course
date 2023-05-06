# 通过函数实现输入任意范围的小数
import re

# 参数: 
#   提示语句
#   开始范围
#   结束范围
# 返回值:
def input_float(msg='请输入一个小数: ', start=None, end=None):
    while 1:
        n = input(msg)
        # 编写正则验证是否是小数
        regex = '^[0-9]*\.[0-9]*$'
        if re.match(regex, n) is not None:
            n = float(n)
            # 判断范围
            if start is not None and end is not None:
                if start <= n <= end:
                    return n 
                else:
                    print(f'您输入的小数不在{start}~{end}之间')
            elif start is not None:
                if start <= n:
                    return n 
                else:
                    print(f'请输入大于等于{start}的小数')
            else:
                return n
        else:
            print('您输入的不是小数')
        pass
    pass
