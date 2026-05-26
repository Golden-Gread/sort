import matplotlib.pyplot as plt
import re
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

str1=""
str2=""
str3=""

def parse_data(filename, content):
    """解析数据文件"""
    data = []
    lines = content.strip().split('\n')
    count = 0
    for line in lines[0:]:  # 跳过第一行标题
        count += 1
        data.append((int(count*100),float(line)))
    return sorted(data, key=lambda x: x[0])  # 按数据量排序

# 您的数据
tout_content = """"""

xzout_content = """"""

content3=""""""

# 解析数据
tout_data = parse_data("", tout_content)
xzout_data = parse_data("", xzout_content)
l3=parse_data("", content3)

# 提取数据点（每10组取一个点用于清晰显示）
sample_rate = 10
tout_x = [d[0] for i, d in enumerate(tout_data) if i % sample_rate == 0]
tout_y = [d[1] for i, d in enumerate(tout_data) if i % sample_rate == 0]
xzout_x = [d[0] for i, d in enumerate(xzout_data) if i % sample_rate == 0]
xzout_y = [d[1] for i, d in enumerate(xzout_data) if i % sample_rate == 0]

out3_x=[d[0] for i, d in enumerate(l3) if i % sample_rate == 0]
out3_y=[d[1] for i, d in enumerate(l3) if i % sample_rate == 0]


# 创建图表
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. 完整数据对比图（使用所有数据）
ax1 = axes[0, 0]
ax1.scatter([d[0] for d in tout_data], [d[1] for d in tout_data], 
            s=10, alpha=0.6, label=str1, c='blue')
ax1.scatter([d[0] for d in xzout_data], [d[1] for d in xzout_data], 
            s=10, alpha=0.6, label=str2, c='red')
ax1.scatter([d[0] for d in l3], [d[1] for d in l3], 
            s=10, alpha=0.6, label=str3, c='green')
ax1.set_xlabel('数据量')
ax1.set_ylabel('耗时 (ms)')
ax1.set_title('{} vs {} vs {} - 完整数据对比'.format(str1, str2, str3))
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. 小数据量区域对比 (0-10000)
ax2 = axes[0, 1]
small_tout = [(x, y) for x, y in tout_data if x <= 10000]
small_xzout = [(x, y) for x, y in xzout_data if x <= 10000]
small_l3 = [(x, y) for x, y in l3 if x <= 10000]
ax2.plot([d[0] for d in small_tout], [d[1] for d in small_tout], 
         'o-', markersize=3, label=str1, c='blue')
ax2.plot([d[0] for d in small_xzout], [d[1] for d in small_xzout], 
         'o-', markersize=3, label=str2, c='red')
ax2.plot([d[0] for d in small_l3], [d[1] for d in small_l3], 
        'o-', markersize=3, label=str3, c='green')
ax2.set_xlabel('数据量')
ax2.set_ylabel('耗时 (ms)')
ax2.set_title('小数据量区域对比 (0-10000)')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. 大数据量区域对比 (10000-50000)
ax3 = axes[1, 0]
large_tout = [(x, y) for x, y in tout_data if x > 10000]
large_xzout = [(x, y) for x, y in xzout_data if x > 10000]
large_l3= [(x, y) for x, y in l3 if x > 10000]
ax3.plot([d[0] for d in large_tout], [d[1] for d in large_tout], 
         'o-', markersize=3, label=str1, c='blue')
ax3.plot([d[0] for d in large_xzout], [d[1] for d in large_xzout], 
         'o-', markersize=3, label=str2, c='red')
ax3.plot([d[0] for d in large_l3], [d[1] for d in large_l3], 
        'o-', markersize=3, label=str3, c='green')
ax3.set_xlabel('数据量')
ax3.set_ylabel('耗时 (ms)')
ax3.set_title('大数据量区域对比 (10000-50000)')
ax3.legend()
ax3.grid(True, alpha=0.3)

# 4. 性能统计对比
ax4 = axes[1, 1]
tout_times = [d[1] for d in tout_data]
xzout_times = [d[1] for d in xzout_data]
l3_times = [d[1] for d in l3]
# 计算统计指标
stats = {
    str1: {
        '平均': np.mean(tout_times),
        '中位数': np.median(tout_times),
        '最大': np.max(tout_times),
        '最小': np.min(tout_times),
        '标准差': np.std(tout_times)
    },
    str2: {
        '平均': np.mean(xzout_times),
        '中位数': np.median(xzout_times),
        '最大': np.max(xzout_times),
        '最小': np.min(xzout_times),
        '标准差': np.std(xzout_times)
    },
    str3:{
        '平均': np.mean(l3_times),
        '中位数': np.median(l3_times),
        '最大': np.max(l3_times),
        '最小': np.min(l3_times),
        '标准差': np.std(l3_times)
    }
}


# 绘制柱状图
x = np.arange(4)
width = 0.35
metrics = ['平均', '中位数', '最大', '最小']
tout_stats = [stats[str1][m] for m in metrics]
xzout_stats = [stats[str2][m] for m in metrics]
l3_stats = [stats[str3][m] for m in metrics]
bars1 = ax4.bar(x - width/2, tout_stats, width, label=str1, alpha=0.8)
bars2 = ax4.bar(x + width/2, xzout_stats, width, label=str2, alpha=0.8)
bars3 = ax4.bar(x + width/2, l3_stats, width, label=str3, alpha=0.8)
ax4.set_xlabel('统计指标')
ax4.set_ylabel('耗时 (ms)')
ax4.set_title('性能统计对比')
ax4.set_xticks(x)
ax4.set_xticklabels(metrics)
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

# 在柱子上添加数值标签
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

