# from random import randint as rd
# redballs=[]
# while len(redballs)!=6:  #当列表的数字不等于6，这是在设置打破while循环的条件。
#     red_ball = rd(1, 33)
#     if red_ball  not in redballs:
#         redballs.append(red_ball)
# blue_ball=rd(1,15)
# redballs.sort()
# print(redballs)
# print(blue_ball)
# from turtle import *
# color('red','red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()
# done()

from turtle import *
color('blue','blue')
begin_fill()
for i in range(3):
    forward(200)
    left(60)
end_fill()
done()