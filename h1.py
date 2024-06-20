#參考chatgpt4-turbo 128k

import random
import copy

# 给定的数据结构
courses = [{'teacher': '  ', 'name':'   ', 'hours': -1}, # 那一節沒上課
{'teacher': '甲', 'name':'機率', 'hours': 2},
{'teacher': '甲', 'name':'線代', 'hours': 3},
{'teacher': '甲', 'name':'離散', 'hours': 3},
{'teacher': '乙', 'name':'視窗', 'hours': 3},
{'teacher': '乙', 'name':'科學', 'hours': 3},
{'teacher': '乙', 'name':'系統', 'hours': 3},
{'teacher': '乙', 'name':'計概', 'hours': 3},
{'teacher': '丙', 'name':'軟工', 'hours': 3},
{'teacher': '丙', 'name':'行動', 'hours': 3},
{'teacher': '丙', 'name':'網路', 'hours': 3},
{'teacher': '丁', 'name':'媒體', 'hours': 3},
{'teacher': '丁', 'name':'工數', 'hours': 3},
{'teacher': '丁', 'name':'動畫', 'hours': 3},
{'teacher': '丁', 'name':'電子', 'hours': 4},
{'teacher': '丁', 'name':'嵌入', 'hours': 3},
{'teacher': '戊', 'name':'網站', 'hours': 3},
{'teacher': '戊', 'name':'網頁', 'hours': 3},
{'teacher': '戊', 'name':'演算', 'hours': 3},
{'teacher': '戊', 'name':'結構', 'hours': 3},
{'teacher': '戊', 'name':'智慧', 'hours': 3}]  # 课程信息列表
teachers = ['甲', '乙', '丙', '丁', '戊']
rooms = ['A', 'B']
slots = ['A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57',]  # 时间段列表

# 生成初始排课计划
def generate_initial_schedule():
    schedule = {}
    for course in courses:
        if course['hours'] > 0:
            for _ in range(course['hours']):
                slot = random.choice(slots)
                room = random.choice(rooms)
                schedule[(slot, room)] = course['name']
    return schedule

# 生成邻近状态
def generate_neighbors(schedule):
    neighbors = []
    keys = list(schedule.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            new_schedule = copy.deepcopy(schedule)
            # 交换两个课程的时间和教室
            new_schedule[keys[i]], new_schedule[keys[j]] = new_schedule[keys[j]], new_schedule[keys[i]]
            neighbors.append(new_schedule)
    return neighbors

# 评估函数（示例：简单评价课程是否均匀分布）
def evaluate(schedule):
    distribution = {}  # 记录每个教师每天的课程数
    for slot, course in schedule.items():
        teacher = [c['teacher'] for c in courses if c['name'] == course][0]
        day = slot[1]  # 假设slot格式为'A11'，其中'1'表示星期几
        if teacher in distribution:
            if day in distribution[teacher]:
                distribution[teacher][day] += 1
            else:
                distribution[teacher][day] = 1
        else:
            distribution[teacher] = {day: 1}
    # 简单评价标准：教师每天的课程数越接近，分数越高
    score = 0
    for teacher in distribution:
        courses_per_day = distribution[teacher].values()
        if max(courses_per_day) - min(courses_per_day) <= 1:
            score += 1 
    return score

# 爬山算法主函数
def hill_climbing():
    current_schedule = generate_initial_schedule()
    current_score = evaluate(current_schedule)
    while True:
        neighbors = generate_neighbors(current_schedule)
        best_neighbor = max(neighbors, key=evaluate)
        best_score = evaluate(best_neighbor)
        if best_score <= current_score:
            break  # 未找到更好的邻近状态
        current_schedule = best_neighbor
        current_score = best_score
    return current_schedule

# 执行算法
final_schedule = hill_climbing()
print("最终排课计划：", final_schedule)
