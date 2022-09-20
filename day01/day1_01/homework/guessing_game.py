import random

# 猜拳游戏
# 0-石头，1-剪刀，2-步

# 玩家猜拳
game_player = int(input("请出拳0-石头，1-剪刀，2-步："))

# 电脑猜拳
computer = random.randint(0,2)
print(f"电脑出拳{computer}")

# 判断玩家胜出
if(game_player == 0 and computer == 1) or (game_player == 1 and computer == 2) or (game_player == 2 and computer == 0):
    print("玩家胜出")

# 判断电脑胜出
elif(game_player == 0 and computer == 2) or (game_player == 1 and computer == 0) or (game_player == 2 and computer == 1):
    print("电脑胜出")

# 判读平局
elif game_player == computer:
    print("平局")
else:
    print("请输入合规数字:0-石头，1-剪刀，2-步")






