import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# パラメータの設定
mu = 0      # 平均
sigma = 1   # 標準偏差

# xの範囲を設定
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

# 正規分布の確率密度関数 (PDF)
pdf = norm.pdf(x, mu, sigma)

# グラフの描画
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, color='skyblue', lw=2)
plt.fill_between(x, pdf, alpha=0.5, color='skyblue')
plt.title(f'Normal Distribution (μ={mu}, σ={sigma})')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid()

# グラフの表示
plt.show()
