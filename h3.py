#參考chatgpt-4 turbo128k

import pulp

# 实例化问题，这里以最大化问题为例
problem = pulp.LpProblem("My_LP_Problem", pulp.LpMaximize)

# 定义决策变量
x = pulp.LpVariable("x", lowBound=0) # x 的下界是 0
y = pulp.LpVariable("y", lowBound=0) # y 的下界是 0

# 添加目标函数
problem += 3*x + 4*y, "Z"

# 添加约束条件
problem += 2*x + y <= 20, "C1"
problem += x + 2*y <= 30, "C2"
problem += x >= 0, "C3"
problem += y >= 0, "C4"

# 解决问题
problem.solve()

# 打印最优解
print("Status:", pulp.LpStatus[problem.status])
print("x = ", pulp.value(x))
print("y = ", pulp.value(y))
print("最优目标函数值 = ", pulp.value(problem.objective))