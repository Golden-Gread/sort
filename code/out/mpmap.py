import matplotlib.pyplot as plt
import numpy as np

# 数据
n = list(range(1, 100))
t_ms = [2.138, 0.022, 0.021, 0.037, 0.021, 0.03, 0.016, 0.017, 0.017, 0.018,
        0.018, 0.017, 0.028, 0.02, 0.034, 0.027, 0.032, 0.027, 0.023, 0.021,
        0.05, 0.021, 0.048, 0.028, 0.026, 0.026, 0.026, 0.03, 0.03, 0.031,
        0.059, 0.052, 0.068, 0.047, 0.08, 0.082, 0.054, 0.065, 0.061, 0.059,
        0.048, 0.068, 0.14, 0.089, 0.072, 0.295, 0.094, 0.08, 0.075, 0.088,
        0.101, 0.092, 0.101, 0.675, 0.102, 0.205, 0.146, 0.144, 0.108, 0.132,
        0.135, 0.359, 0.118, 0.145, 0.128, 0.142, 0.165, 0.724, 0.319, 0.124,
        0.166, 0.22, 0.16, 0.15, 0.17, 0.201, 0.17, 0.162, 0.18, 0.435, 0.849,
        0.373, 0.215, 0.244, 0.211, 0.172, 0.239, 0.175, 0.212, 0.4, 0.545,
        0.318, 0.208, 0.39, 0.209, 0.214, 0.269, 0.234, 0.229]

# 创建图表
plt.figure(figsize=(12, 8))

# 散点图
plt.scatter(n, t_ms, alpha=0.7, color='blue', s=30)
plt.title('Bubble Sort 运行时间 vs 数组规模', fontsize=14, fontweight='bold')
plt.xlabel('数组规模 n', fontsize=12)
plt.ylabel('运行时间 (ms)', fontsize=12)
plt.grid(True, alpha=0.3)

# 由于第一个点(1, 2.138)太大影响比例，我们同时画一个去掉第一个点的图
plt.figure(figsize=(12, 8))
plt.scatter(n[1:], t_ms[1:], alpha=0.7, color='red', s=30)
plt.title('Bubble Sort 运行时间 vs 数组规模 (去掉 n=1)', fontsize=14, fontweight='bold')
plt.xlabel('数组规模 n', fontsize=12)
plt.ylabel('运行时间 (ms)', fontsize=12)
plt.grid(True, alpha=0.3)

# 为了观察 O(n²) 趋势，我们画 n² 与 t 的关系
plt.figure(figsize=(12, 8))
n_squared = [x**2 for x in n[1:]]
plt.scatter(n_squared, t_ms[1:], alpha=0.7, color='green', s=30)
plt.title('运行时间 vs n²', fontsize=14, fontweight='bold')
plt.xlabel('n²', fontsize=12)
plt.ylabel('运行时间 (ms)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 输出一些统计信息
print(f"时间范围: {min(t_ms[1:]):.3f} ~ {max(t_ms[1:]):.3f} ms")
print(f"平均时间 (n>=2): {np.mean(t_ms[1:]):.3f} ms")
print(f"时间标准差: {np.std(t_ms[1:]):.3f} ms")

# 计算相关系数
correlation = np.corrcoef(n[1:], t_ms[1:])[0, 1]
print(f"n 与 t 的相关系数: {correlation:.3f}")

correlation_sq = np.corrcoef(n_squared, t_ms[1:])[0, 1]
print(f"n² 与 t 的相关系数: {correlation_sq:.3f}")