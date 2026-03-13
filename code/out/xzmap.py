import matplotlib.pyplot as plt
import numpy as np

# 选择排序数据
n = list(range(100, 10100, 100))
t_ms = [1.872, 0.335, 0.569, 0.919, 1.685, 2.066, 2.779, 3.571, 5.61, 5.68,
        7.505, 8.153, 9.837, 11.849, 13.027, 15.201, 16.391, 18.577, 20.843, 23.032,
        25.765, 27.438, 30.268, 32.721, 35.596, 38.387, 41.422, 44.871, 48.136, 52.758,
        56.23, 59.053, 61.272, 66.436, 69.818, 73.173, 78.374, 82.767, 85.697, 89.784,
        94.666, 98.881, 105.286, 108.804, 113.353, 120.449, 125.156, 129.675, 135.414, 141.299,
        146.664, 150.995, 156.56, 166.265, 170.224, 175.17, 183.387, 187.557, 196.649, 200.09,
        207.276, 216.075, 220.129, 228.811, 234.664, 242.039, 248.939, 257.334, 263.741, 272.781,
        278.918, 287.159, 294.94, 303.136, 309.844, 330.735, 333.669, 335.494, 344.972, 352.795,
        362.333, 376.174, 384.83, 389.577, 401.166, 407.675, 419.209, 427.084, 437.359, 454.761,
        488.009, 527.183, 532.286, 540.18, 527.674, 508.194, 601.649, 526.198, 546.86, 555.047]

plt.figure(figsize=(14, 8))

# 散点图
plt.scatter(n, t_ms, alpha=0.7, color='green', s=30, label='Selection Sort')

# O(n²) 趋势线
n_array = np.array(n)
coefficients = np.polyfit(n_array, t_ms, 2)
trend_curve = np.poly1d(coefficients)
n_trend = np.linspace(100, 10000, 100)
plt.plot(n_trend, trend_curve(n_trend), 'r--', linewidth=2, label='O(n^2) Trend')

plt.title('Selection Sort Performance (n=100 to 10000)', fontsize=16, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Running Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# 添加性能公式
formula = f't ≈ {coefficients[0]:.2e}·n² + {coefficients[1]:.2e}·n + {coefficients[2]:.2f}'
plt.text(100, 500, formula, fontsize=11, bbox=dict(boxstyle="round,pad=0.3", facecolor="white"))

plt.tight_layout()
plt.show()

# 统计分析
print("=== Statistical Analysis ===")
print(f"Data range: n from {min(n)} to {max(n)}")
print(f"Time range: {min(t_ms):.3f} ~ {max(t_ms):.3f} ms")

# 计算相关系数
correlation_n2 = np.corrcoef([x**2 for x in n], t_ms)[0, 1]
print(f"Correlation between n^2 and t: {correlation_n2:.6f}")

# 计算常数因子
k_values = [t / (n_val**2) for n_val, t in zip(n, t_ms)]
avg_k = np.mean(k_values)
std_k = np.std(k_values)
print(f"Average constant factor k: {avg_k:.2e} ms/operation")
print(f"Standard deviation of k: {std_k:.2e}")