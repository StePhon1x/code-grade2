# 游戏刚开始
# 范围    grid_size  
# 蛇  列表  snake_body
'''
snake_body
[
    [], #坐标 - 蛇头
    [], #坐标 - 蛇身
    [], #坐标 - 蛇身
]
食物
food = [0,0]

坐标系
[
    [' ',' ',' '], 
    [' ',' ',' '], 
    [' ',' ',' ']
]

显示效果
[ ] [F] [ ] 
[ ] [ ] [ ] 
[ ] [O] [ ] 
'''
import random
# 网格显示函数
def print_grid(grid):
    for row in grid:
        for col in row:
            print(f"[{col}]", end = " ")
        print()
        
def move_snake(direction,head_row, head_col):
    if direction == 'w': # 上
        return head_row - 1, head_col
    elif direction == 's': # 下
        return head_row + 1, head_col
    elif direction == 'a': # 左
        return head_row, head_col - 1
    elif direction == 'd': # 右
        return head_row, head_col + 1

def is_valid_move(head_row,head_col,grid_size,snake_body):    #判断蛇是否撞墙，是否会撞到自己
    if head_row < 0 or head_row >= grid_size or head_col < 0 or head_col >= grid_size:
        print('游戏结束！你撞墙了。')
        return False
    if [head_row,head_col] in snake_body:
        print('游戏结束！你撞到自己了。')
        return False
    return True
# 网格大小、蛇、食品位置
grid_size = 3
snake_body = [[random.randint(0,grid_size-1),random.randint(0,grid_size-1)]]
food_location = [random.randint(0,grid_size-1),random.randint(0,grid_size-1)]
# 坐标系
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
print(snake_body)
print(food_location)
for i, (row,col) in enumerate(snake_body):
    if i == 0:  # 给蛇头渲染
        grid[row][col] = 'O'
    else:       # 给蛇身渲染    
        grid[row][col] = '*'
grid[food_location[0]][food_location[1]] = 'F'

# wasd 接收蛇移动方向
while True:
    direction = input("输入前后左右(wasd):").lower()
    if direction in ['w','a','s','d']:
        break
    else:
        print("无效输入，请重新输入.")

head_row, head_col = snake_body[0]

head_row, head_col = move_snake(direction,head_row, head_col) # 新蛇头位置
print(head_row, head_col)


print(grid)
print_grid(grid)

