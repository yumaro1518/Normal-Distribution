import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib 
from scipy.stats import norm

# 日本語フォントの設定
plt.rcParams['font.family'] = 'IPAexGothic'  # 使用する日本語フォントを指定
plt.rcParams['axes.unicode_minus'] = False   # マイナス記号を正しく表示
# 標準正規分布のパラメータ
mu = 0      # 平均
sigma = 1   # 標準偏差

# xの範囲を設定
x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 1000)

# 標準正規分布の確率密度関数 (PDF)
pdf = norm.pdf(x, mu, sigma)

# 下位25%分、中央25%分、上位25%分の境界を計算
lower_bound = norm.ppf(0.25)  # 下位25%分の境界
upper_bound = norm.ppf(0.75)  # 上位25%分の境界
lower_bound10  = norm.ppf(0.45)
upper_bound10  = norm.ppf(0.55)
# グラフの描画
plt.figure(figsize=(10, 6))

# 下位25%分の領域
plt.fill_between(x, pdf, where=(x < lower_bound), color='lightblue', label='Lower 25%')

# 中央25%分の領域
plt.fill_between(x, pdf, where=(x >= lower_bound10) & (x <= upper_bound10), color='lightgreen', label='Central 10%')

# 上位25%分の領域
plt.fill_between(x, pdf, where=(x > upper_bound), color='lightcoral', label='Upper 25%')

# 正規分布の曲線を描画
plt.plot(x, pdf, color='black', lw=2)
plt.title('標準正規分布と割合別色分け')
plt.xlabel('確率変数')
plt.ylabel('確率密度')
plt.axvline(lower_bound, color='blue', linestyle='--', lw=1, label='25th Percentile')
plt.axvline(upper_bound, color='red', linestyle='--', lw=1, label='75th Percentile')
plt.legend()
plt.grid()

# グラフの表示
plt.show()
