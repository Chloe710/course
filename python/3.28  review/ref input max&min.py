def check_input():
    while True:
        num = input('please input a number')
        if num.isdigit() == True:
            break
    v = int(num)  # num = input('请输入一个数值：')
    return v

n=5
nums=[]
for i in range(n):
    result = check_input()
    nums.append(result)

print(f'the maximum number is {max(nums)},the minimum is {min(nums)}')