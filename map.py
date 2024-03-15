from models import RobotDelivery
from collections import deque

# map -> https://miro.com/welcomeonboard/eG9MVm53TUJYQjRtOTNkSEhnamRWM2RCYVBDUklUckVMN3k3OUdsb2hQVjdJcEhpSmY1NjVJUnc0S3V4OHJZVXwzNDU4NzY0NTM2MDUzNzg0NTg4fDI=?share_link_id=306437873724
maps = [[4, 2, 1, 2, 4, 2, 1, 0, 4, 4],
       [2, 2, 1, 0, 2, 2, 1, 0, 2, 2],
       [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
       [2, 0, 1, 1, 1, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 3, 1, 1, 1, 1, 1],
       [1, 2, 2, 1, 1, 1, 0, 1, 1, 1],
       [1, 2, 2, 1, 1, 1, 1, 2, 2, 1],
       [1, 1, 1, 1, 0, 0, 1, 2, 4, 0],
       [1, 1, 2, 2, 4, 2, 1, 2, 2, 1],
       [1, 1, 2, 4, 4, 2, 1, 1, 1, 1]]
# 0 - преграда
# 1 - дорога для робота
# 2 - адреса доставки
# 3 - точка отправки
# 4 - недоступная зона доставки


def print_map(map):
    print("Путь робота")
    for i in map:
        row = ''
        for j in i:
            row += str(j) + ' '
        print(row)
    print('_' * 10)


def find_points(bot_map, start, end):
    # Определяем возможные направления движения: вправо, вниз, влево, вверх
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Размеры матрицы
    rows = 10
    cols = 10
    
    # список посещенных ячеек
    visited = [[False] * cols for _ in range(rows)]
    
    # Отмечаем точку отправки как посещенную
    visited[start[0]][start[1]] = True
    
    # Используем очередь для BFS
    queue = deque([(start, [])])
    
    while queue:
        current, path = queue.popleft()
        x, y = current
        
        # Если мы достигли точки доставки, возвращаем найденный путь
        if current == end:
            return path + [current]
        
        # Иначе ищем соседние доступные ячейки
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # можем мы посетить эту ячейку
            if 0 <= nx < rows and 0 <= ny < cols and bot_map[nx][ny] in [1, 9] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [current]))



def find_route(bot: RobotDelivery):
    
    start = (4, 4)
    end = (bot.targetY, bot.targetX)
    
    bot.route = maps
    bot.route[bot.targetY][bot.targetX] = 9
    
    route = find_points(bot.route, start, end)
    
    for point in route:
        maps[point[0]][point[1]] = 'X'
    print_map(bot.route)