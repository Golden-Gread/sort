import matplotlib.pyplot as plt
import numpy as np

# 解析第一个文件（冒泡排序）
# 注意：文件中的乱码可能是编码问题，但我只提取数字
bubble_n = list(range(100, 10100, 100))
bubble_times = [2.342, 0.674, 1.466, 3.068, 5.346, 7.472, 9.645, 11.64, 15.293, 20.287,
                22.192, 28.026, 33.922, 37.902, 42.53, 48.371, 55.998, 60.885, 69.749, 76.92,
                85.742, 93.624, 98.499, 108.364, 121.223, 130.136, 140.942, 154.912, 168.901, 176.118,
                184.358, 198.71, 246.64, 221.081, 230.862, 250.137, 274.738, 287.346, 298.961, 307.402,
                330.371, 336.417, 362.17, 378.99, 392.377, 413.921, 438.627, 451.63, 481.589, 504.573,
                566.459, 646.229, 622.867, 568.266, 597.78, 626.529, 694.361, 665.205, 724.289, 790.972,
                743.116, 782.489, 812.401, 818.929, 822.657, 851.543, 901.406, 964.454, 956.816, 954.34,
                976.94, 1060.51, 1040.63, 1061.24, 1118.59, 1150.62, 1136.26, 1186.05, 1245.93, 1183.25,
                1225.51, 1337.05, 1405.25, 1419.75, 1398.91, 1401.71, 1453.38, 1762.1, 1553.04, 1603.24,
                1651.34, 1658.86, 1964.21, 1959.91, 1781.65, 1819.81, 1791.11, 1814.9, 2192.06, 2006.42]

# 解析第二个文件（选择排序）
selection_n = list(range(100, 10100, 100))
selection_times = [2.178, 0.29, 0.509, 1.468, 1.793, 2.317, 3.452, 4.517, 4.944, 7.041,
                   7.491, 9.204, 10.631, 12.65, 15.336, 16.548, 18.043, 22.198, 23.933, 25.917,
                   27.184, 30.691, 34.954, 37.808, 40.227, 42.07, 46.198, 49.503, 54.693, 54.238,
                   62.675, 64.635, 76.306, 116.29, 105.136, 119.38, 106.166, 89.499, 94.478, 98.815,
                   103.693, 105.415, 111.499, 119.931, 123.084, 143.689, 133.498, 149.707, 147.956, 164.509,
                   165.138, 171.371, 182.052, 187.86, 198.717, 194.222, 213.63, 230.622, 230.518, 227.053,
                   261.009, 245.937, 269.24, 255.628, 327.065, 281.567, 288.339, 299.684, 300.766, 307.118,
                   322.802, 331.705, 358.763, 359.507, 376.592, 369.026, 375.64, 382.369, 391.451, 403.918,
                   415.246, 425.132, 443.301, 450.937, 456.852, 474.778, 486.525, 482.643, 498.031, 573.621,
                   547.795, 540.145, 566.956, 618.347, 592.18, 648.364, 831.292, 695.181, 650.97, 681.608]

# 创建对比图表
plt.figure(figsize=(16, 10))

# 1. 原始数据散点图
plt.subplot(2, 2, 1)
plt.scatter(bubble_n, bubble_times, alpha=0.6, color='blue', s=20, label='Bubble Sort')
plt.scatter(selection_n, selection_times, alpha=0.6, color='green', s=20, label='Selection Sort')
plt.title('Raw Data Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.yscale('linear')

# 2. 对数尺度图，更清晰地显示趋势
plt.subplot(2, 2, 2)
plt.scatter(bubble_n, bubble_times, alpha=0.6, color='blue', s=20, label='Bubble Sort')
plt.scatter(selection_n, selection_times, alpha=0.6, color='green', s=20, label='Selection Sort')
plt.title('Log-Log Scale Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xscale('log')
plt.yscale('log')

# 3. 时间对比（选择排序/冒泡排序）
plt.subplot(2, 2, 3)
ratio = [s/b for s, b in zip(selection_times, bubble_times)]
plt.scatter(bubble_n, ratio, alpha=0.6, color='red', s=20)
plt.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
plt.title('Selection Sort / Bubble Sort Time Ratio', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time Ratio', fontsize=12)
plt.grid(True, alpha=0.3)

# 4. 性能趋势线
plt.subplot(2, 2, 4)

# 拟合冒泡排序趋势线 (O(n²))
bubble_coeff = np.polyfit(bubble_n, bubble_times, 2)
bubble_fit = np.poly1d(bubble_coeff)
n_range = np.linspace(100, 10000, 100)
plt.plot(n_range, bubble_fit(n_range), 'b-', linewidth=2, label='Bubble Sort O(n²)')

# 拟合选择排序趋势线 (O(n²))
selection_coeff = np.polyfit(selection_n, selection_times, 2)
selection_fit = np.poly1d(selection_coeff)
plt.plot(n_range, selection_fit(n_range), 'g-', linewidth=2, label='Selection Sort O(n²)')

plt.title('Quadratic Trend Lines', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# 统计分析
print("=== PERFORMANCE ANALYSIS ===")
print(f"Data range: n from 100 to 10000")

# 关键点比较
key_points = [1000, 2000, 5000, 10000]
print("\nKey Performance Points:")
print("n\tBubble(ms)\tSelection(ms)\tRatio\tSpeed Advantage")
print("-" * 60)

for n_val in key_points:
    idx = n_val//100 - 1
    bubble_t = bubble_times[idx]
    selection_t = selection_times[idx]
    ratio = bubble_t / selection_t if selection_t > 0 else 0
    print(f"{n_val}\t{bubble_t:.1f}\t\t{selection_t:.1f}\t\t{ratio:.2f}\t{ratio:.1f}x")

# 整体统计
print("\n=== OVERALL STATISTICS ===")
print(f"Bubble Sort - Average time: {np.mean(bubble_times):.1f} ms")
print(f"Selection Sort - Average time: {np.mean(selection_times):.1f} ms")

overall_ratio = np.mean([b/s for b, s in zip(bubble_times, selection_times) if s > 0])
print(f"Average performance ratio (Bubble/Selection): {overall_ratio:.2f}")

# 复杂度验证
print("\n=== COMPLEXITY VERIFICATION ===")
print("Verifying O(n²) growth:")

# 检查n=1000到n=2000的增长
idx_1000 = 9  # n=1000
idx_2000 = 19  # n=2000
idx_4000 = 39  # n=4000

bubble_growth_2x = bubble_times[idx_2000] / bubble_times[idx_1000]
selection_growth_2x = selection_times[idx_2000] / selection_times[idx_1000]
expected_growth_2x = 4.0  # (2000/1000)² = 4

print(f"Bubble Sort (1000→2000): {bubble_growth_2x:.2f}x, Expected: {expected_growth_2x}x")
print(f"Selection Sort (1000→2000): {selection_growth_2x:.2f}x, Expected: {expected_growth_2x}x")

# 常数因子计算
print("\n=== CONSTANT FACTORS ===")
bubble_k = np.mean([t/(n**2) for n, t in zip(bubble_n, bubble_times) if n >= 1000])
selection_k = np.mean([t/(n**2) for n, t in zip(selection_n, selection_times) if n >= 1000])

print(f"Bubble Sort constant factor k: {bubble_k:.2e} ms/operation")
print(f"Selection Sort constant factor k: {selection_k:.2e} ms/operation")
print(f"Selection Sort is {bubble_k/selection_k:.1f} times faster (lower constant factor)")