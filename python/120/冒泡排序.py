# 列表
list1 = [8, 2, 16, 7, 13, -8]

# # 第一次
# if list1[0] > list1[1]:
#     list1[0], list1[1] = list1[1], list1[0]

# print(f'第一次比较的结果: {list1}')

# # 第二次
# if list1[1] > list1[2]:
#     list1[1], list1[2] = list1[2], list1[1]
# print(f'第二次比较的结果: {list1}')

# 可以使用循环优化一下
# IndexError: list index out of range
# for i in range(len(list1) - 1 - 0):
#     if list1[i] > list1[i + 1]:
#         list1[i], list1[i + 1] = list1[i + 1], list1[i]
# print(f'第{i + 1}次比较的结果: {list1}')

# for i in range(len(list1) - 1 - 1):
#     if list1[i] > list1[i + 1]:
#         list1[i], list1[i + 1] = list1[i + 1], list1[i]
# print(f'第{i + 1}次比较的结果: {list1}')
# for i in range(len(list1) - 1 - 2):
#     if list1[i] > list1[i + 1]:
#         list1[i], list1[i + 1] = list1[i + 1], list1[i]
# print(f'第{i + 1}次比较的结果: {list1}')

# 最终代码
# 外层循环-1是为少循环一次
for j in range(len(list1) - 1):
    # 内层循环-1是为防止索引越界
    for i in range(len(list1) - 1 - j):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
    print(f'第{j + 1}次比较的结果: {list1}')