#參考chatgpt-4 turbo128k

import random
import math

# 定义城市坐标
citys = [
    (0,3), (0,0),
    (0,2), (0,1),
    (1,0), (1,3),
    (2,0), (2,3),
    (3,0), (3,3),
    (3,1), (3,2)
]

# 计算两点间的欧几里得距离
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# 计算完整路径的总距离
def total_path_distance(path):
    distance = 0
    for i in range(len(path)):
        distance += euclidean_distance(citys[path[i - 1]], citys[path[i]])
    return distance

# 生成初试解（随机路径）
def random_solution():
    path = list(range(len(citys)))
    random.shuffle(path)
    return path

# 生成路径的邻域解（通过交换两个城市的位置来生成新的路径）
def get_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# 爬山算法
def hill_climbing():
    current_solution = random_solution()
    current_distance = total_path_distance(current_solution)
    neighbors = get_neighbors(current_solution)
    
    # 搜索邻域中更优的解
    for neighbor in neighbors:
        neighbor_distance = total_path_distance(neighbor)
        if neighbor_distance < current_distance:
            current_solution, current_distance = neighbor, neighbor_distance

    return current_solution, current_distance

# 运行爬山算法
best_solution, best_distance = hill_climbing()

print('Best Path:', best_solution)
print('Best Path Distance:', best_distance)