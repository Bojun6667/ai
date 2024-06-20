#參考chatgpt-4 turbo128k

from scipy.optimize import linprog

# 目标函数的系数（注意我们用负数来表示最大化问题）
c = [-3, -2, -5]

# 不等式约束矩阵左侧
A = [[1, 1, 0], [2, 0, 1], [0, 1, 2]]

# 不等式约束矩阵右侧
b = [10, 9, 11]

# 变量界限，x,y,z都需要大于等于0
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

# 解决线性规划问题
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

if result.success:
    # 注意,由于我们最小化了目标函数的负数，因此这里取-fun的负数来获得最大化的结果
    print(f'最优解: x={result.x[0]}, y={result.x[1]}, z={result.x[2]}')
    print(f'目标函数最大值: {-result.fun}')
else:
    print('线性规划问题无解')
