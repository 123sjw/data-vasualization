import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# 数据
x = [1, 2, 3, 4, 5]
y1 = [1, 5, 4, 2, 7]
y2 = [2, 3, 3, 1, 4]
y3 = [5, 2, 3, 4, 1]

# 定义中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 绘制折线图
plt.plot(x, y1, label="折线图1")
plt.plot(x, y2, label="折线图2")
plt.plot(x, y3, label="折线图3")

# 添加图例
plt.legend(loc="upper right")

# 添加标题和标签
plt.title("折线图示例")
plt.xlabel("横坐标")
plt.ylabel("纵坐标")

# 显示图形22222222222222222222222222222222
plt.show()