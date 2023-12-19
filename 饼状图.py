###饼图

import matplotlib.pyplot as plt

# 定义数据
labels = ['就业(8人)', '考研(25人）', '保研（3人）']
sizes = [8, 25, 3]
colors = ['red', 'yellow', 'green']

# 生成饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# 设置饼图的长宽比，使其变成一个圆形
plt.axis('equal')

# 添加主标题
plt.title("智能2001毕业去向情况(36人)")

# 设置标签为中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 字体可以根据需要进行调整

# 显示图形
plt.show()


