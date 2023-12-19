###柱状图

import matplotlib.pyplot as plt

# 定义数据
labels = ['苹果', '香蕉', '橙子', '葡萄']
heights = [15, 30, 45, 10]
colors = ['red', 'blue', 'green', 'yellow']

# 生成柱状图
plt.bar(labels, heights, color=colors)

# 添加主标题
plt.title("水果销量")
plt.xlabel("x轴")
plt.ylabel("y轴")

# 设置标签为中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 字体可以根据需要进行调整

# 显示图形
plt.show()

# 复杂柱状图(三个纵坐标，一个横坐标）
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义数据
labels = ['苹果', '香蕉', '橙子', '葡萄']
values1 = [15, 30, 45, 10]
values2 = [20, 35, 40, 15]
values3 = [1, 2, 3, 4]

# 设置宽度和位置
width = 0.2
x = np.arange(len(labels))

# 生成柱状图
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, values1, width, label='销量1')
rects2 = ax.bar(x , values2, width, label='销量2')
y3=ax.bar(x+width,values3,width,label="销量3")

# 设置标签和标题为中文
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 字体可以根据需要进行调整
plt.title("水果销量")
plt.xlabel("x轴")
plt.ylabel("y轴")

# 添加图例
ax.legend()

# 显示图形
plt.show()
"""
