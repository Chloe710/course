# 通过python代码实现双色球中奖号码
# 双色球的规则
# 红球: 1~33,选6个（随机不重复）
# 蓝球: 1~16,选1个
# 1. 需要随机数的支持
# 2. 通过循环来保存红球
# 3. 输出结果
import random as r

# 先 生成33个红球
red_balls = [i for i in range(1, 34)]
# 再 生成16个蓝球
blue_ball = [i for i in range(1, 17)]

# 生成中奖蓝球
win_blue_ball = blue_ball[r.randint(0, 15)]
win_blue_ball = f'0{win_blue_ball}' if win_blue_ball < 10 else f'{win_blue_ball}'

# 生成中奖红球
win_red_ball = set()
while len(win_red_ball) < 6:
    # 每次获取中奖号码的时候首先打乱顺序，然后在随机选取中奖号码
    r.shuffle(red_balls)
    n = red_balls[r.randint(0, 32)]
    win_red_ball.add(n)
    pass

win_red_ball = list(win_red_ball)
win_red_ball.sort()

win_red_ball = [f'0{i}' if i < 10 else f'{i}' for i in win_red_ball]

print(f'中奖红球: {win_red_ball}')
print(f'中奖蓝球: {win_blue_ball}')