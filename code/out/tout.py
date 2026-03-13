import matplotlib.pyplot as plt
import numpy as np

# 桶排序数据
bucket_n = list(range(100, 10100, 100))
bucket_times = [1.729, 0.038, 0.049, 0.1, 0.06, 0.074, 0.081, 0.087, 0.092, 0.1,
                0.114, 0.159, 0.343, 0.153, 0.139, 0.147, 0.226, 0.162, 0.171, 0.177,
                0.198, 0.257, 0.197, 0.204, 0.215, 0.405, 0.412, 0.35, 0.291, 0.272,
                0.271, 0.269, 0.299, 0.281, 0.288, 0.358, 0.302, 0.311, 0.366, 0.323,
                0.391, 0.376, 0.587, 0.418, 0.458, 0.388, 0.471, 0.403, 0.454, 0.418,
                0.498, 0.432, 0.463, 0.485, 0.466, 0.523, 0.585, 0.557, 0.607, 0.541,
                0.971, 0.57, 0.565, 0.587, 0.53, 0.537, 0.607, 0.546, 0.596, 0.642,
                0.616, 0.584, 0.607, 0.637, 0.767, 0.677, 0.616, 0.687, 0.972, 0.697,
                0.695, 0.95, 0.745, 0.74, 0.965, 0.925, 0.767, 0.776, 0.788, 0.8,
                0.762, 0.785, 1.098, 0.841, 0.933, 0.847, 0.83, 0.913, 0.952, 0.869]

# 之前的数据
# 冒泡排序
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

# 选择排序
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

# 1. 四种排序算法对比（对数尺度）
plt.subplot(2, 2, 1)
plt.scatter(bucket_n, bucket_times, alpha=0.7, color='red', s=20, label='Bucket Sort')
plt.scatter(selection_n, selection_times, alpha=0.7, color='green', s=20, label='Selection Sort')
plt.scatter(bubble_n, bubble_times, alpha=0.7, color='blue', s=20, label='Bubble Sort')

plt.title('Four Sorting Algorithms Comparison (Log Scale)', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xscale('log')
plt.yscale('log')

# 2. 桶排序细节（线性尺度）
plt.subplot(2, 2, 2)
plt.scatter(bucket_n, bucket_times, alpha=0.7, color='red', s=20)
plt.title('Bucket Sort Performance (Linear Scale)', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)

# 添加线性趋势线
bucket_coeff = np.polyfit(bucket_n, bucket_times, 1)
bucket_fit = np.poly1d(bucket_coeff)
n_range = np.linspace(100, 10000, 100)
plt.plot(n_range, bucket_fit(n_range), 'r--', linewidth=2, 
         label=f'Linear fit: t = {bucket_coeff[0]:.4f}n + {bucket_coeff[1]:.3f}')
plt.legend()

# 3. 性能加速比
plt.subplot(2, 2, 3)
# 计算加速比（相对于选择排序）
speedup_vs_selection = [s/b for s, b in zip(selection_times, bucket_times) if b > 0]
speedup_vs_bubble = [b/bu for b, bu in zip(bubble_times, bucket_times) if bu > 0]

plt.scatter(bucket_n[:len(speedup_vs_selection)], speedup_vs_selection, 
           alpha=0.7, color='green', s=20, label='vs Selection Sort')
plt.scatter(bucket_n[:len(speedup_vs_bubble)], speedup_vs_bubble,
           alpha=0.7, color='blue', s=20, label='vs Bubble Sort')

plt.title('Bucket Sort Speedup Ratio', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Speedup Ratio', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.yscale('log')

# 4. 时间复杂度对比
plt.subplot(2, 2, 4)

# 桶排序：线性拟合
plt.plot(n_range, bucket_fit(n_range), 'r-', linewidth=3, label='Bucket Sort ~O(n)')

# 选择排序：二次拟合
selection_coeff = np.polyfit(selection_n, selection_times, 2)
selection_fit = np.poly1d(selection_coeff)
plt.plot(n_range, selection_fit(n_range), 'g-', linewidth=2, label='Selection Sort O(n²)')

# 冒泡排序：二次拟合
bubble_coeff = np.polyfit(bubble_n, bubble_times, 2)
bubble_fit = np.poly1d(bubble_coeff)
plt.plot(n_range, bubble_fit(n_range), 'b-', linewidth=2, label='Bubble Sort O(n²)')

plt.title('Time Complexity Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Data Size n', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.yscale('log')

plt.tight_layout()
plt.show()

# 统计分析
print("=== BUCKET SORT PERFORMANCE ANALYSIS ===")
print(f"Data range: n from 100 to 10000")
print(f"Time range: {min(bucket_times[1:]):.3f} ~ {max(bucket_times):.3f} ms")
print(f"Average time: {np.mean(bucket_times):.3f} ms")

# 关键点比较
print("\n=== KEY PERFORMANCE COMPARISON ===")
key_points = [1000, 2000, 5000, 10000]
print("n\tBucket\t\tSelection\tBubble\t\tBucket/Selection\tBucket/Bubble")
print("-" * 90)

for n_val in key_points:
    idx = n_val//100 - 1
    bucket_t = bucket_times[idx]
    selection_t = selection_times[idx]
    bubble_t = bubble_times[idx]
    
    ratio_vs_selection = selection_t / bucket_t if bucket_t > 0 else 0
    ratio_vs_bubble = bubble_t / bucket_t if bucket_t > 0 else 0
    
    print(f"{n_val}\t{bucket_t:.3f} ms\t{selection_t:.1f} ms\t{bubble_t:.1f} ms\t{ratio_vs_selection:.0f}x\t\t\t{ratio_vs_bubble:.0f}x")

# 复杂度分析
print("\n=== COMPLEXITY ANALYSIS ===")
print("Bucket Sort growth analysis:")
print(f"  Linear fit: t = {bucket_coeff[0]:.6f}n + {bucket_coeff[1]:.3f}")
print(f"  R² value: {np.corrcoef(bucket_n, bucket_times)[0,1]**2:.6f}")

# 检查增长比例
print("\nGrowth verification:")
for from_n, to_n in [(1000, 2000), (2000, 4000), (5000, 10000)]:
    idx_from = from_n//100 - 1
    idx_to = to_n//100 - 1
    
    actual_growth = bucket_times[idx_to] / bucket_times[idx_from]
    linear_growth = to_n / from_n  # 线性增长的期望
    
    print(f"  {from_n}→{to_n}: Actual {actual_growth:.2f}x, Expected (linear) {linear_growth:.1f}x")

# 桶排序的理论时间复杂度
print("\n=== BUCKET SORT CHARACTERISTICS ===")
print("Theoretical time complexity: O(n + k)")
print("Where n = number of elements, k = number of buckets")
print("Best case: O(n) when elements are uniformly distributed")
print("Worst case: O(n²) when all elements fall into the same bucket")
print("\nFrom the data, we observe nearly linear growth, suggesting:")
print("1. Good bucket distribution strategy")
print("2. Efficient inner sorting within buckets")
print("3. Well-chosen bucket count")