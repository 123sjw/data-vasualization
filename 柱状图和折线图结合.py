import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 数据
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 7, 12, 9]
y2 = [5, 8, 10, 6, 3]

# 创建一个图形和轴对象
fig, ax1 = plt.subplots()

# 绘制柱状图
ax1.bar(x, y1, color='blue', label='柱状图')

# 绘制折线图
ax1.plot(x, y2, color='red', label='折线图')


ax1.set_ylabel('纵坐标', color='black')

# 图例
ax1.legend(loc='upper center')
# 设置轴标签和标题
ax1.set_xlabel('横坐标')
plt.title('柱状图和折线图混合图')

# 显示图形
plt.show()